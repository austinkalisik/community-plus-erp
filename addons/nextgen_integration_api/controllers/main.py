import hmac
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class NextGenIntegrationController(http.Controller):

    def _response(self, data, status=200):
        return request.make_json_response(data, status=status)

    def _authorized(self):
        expected = (
            request.env["ir.config_parameter"]
            .sudo()
            .get_param("nextgen.integration.token")
            or ""
        )

        header = request.httprequest.headers.get("Authorization", "")

        supplied = ""
        if header.startswith("Bearer "):
            supplied = header[7:].strip()

        return bool(
            expected
            and supplied
            and hmac.compare_digest(expected, supplied)
        )

    @http.route(
        "/nextgen/api/v1/health",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
    )
    def health(self, **kwargs):
        company = request.env.company.sudo()

        return self._response({
            "status": "ok",
            "service": "NextGen OneSuite Integration API",
            "database": request.env.cr.dbname,
            "company": company.name,
            "currency": company.currency_id.name,
        })

    @http.route(
        "/nextgen/api/v1/orders",
        type="http",
        auth="public",
        methods=["POST"],
        csrf=False,
    )
    def receive_order(self, **kwargs):

        if not self._authorized():
            return self._response({
                "status": "error",
                "message": "Unauthorized",
            }, 401)

        payload = request.httprequest.get_json(silent=True) or {}

        source = str(payload.get("source") or "").strip().lower()
        order_number = str(payload.get("order_number") or "").strip()
        items = payload.get("items") or []
        dry_run = bool(payload.get("dry_run"))

        if source != "b2b":
            return self._response({
                "status": "error",
                "message": "source must be b2b",
            }, 422)

        if not order_number:
            return self._response({
                "status": "error",
                "message": "order_number is required",
            }, 422)

        if not isinstance(items, list) or not items:
            return self._response({
                "status": "error",
                "message": "At least one order item is required",
            }, 422)

        company = request.env.company.sudo()
        incoming_currency = str(
            payload.get("currency") or company.currency_id.name
        ).upper()

        if incoming_currency != company.currency_id.name.upper():
            return self._response({
                "status": "error",
                "message": "Currency mismatch",
                "incoming_currency": incoming_currency,
                "onesuite_currency": company.currency_id.name,
            }, 422)

        if dry_run:
            return self._response({
                "status": "ok",
                "dry_run": True,
                "source": source,
                "order_number": order_number,
                "items": len(items),
                "currency": company.currency_id.name,
                "message": "Payload accepted. No records created.",
            })

        external_reference = f"B2B:{order_number}"

        SaleOrder = request.env["sale.order"].sudo()

        existing = SaleOrder.search([
            ("client_order_ref", "=", external_reference)
        ], limit=1)

        if existing:
            return self._response({
                "status": "ok",
                "result": "duplicate",
                "sale_order_id": existing.id,
                "sale_order": existing.name,
                "state": existing.state,
                "amount_total": existing.amount_total,
            })

        buyer = payload.get("buyer") or {}

        company_name = (
            buyer.get("company_name")
            or buyer.get("name")
            or "B2B Customer"
        )

        email = (
            buyer.get("email")
            or buyer.get("invoice_email")
            or ""
        ).strip()

        phone = str(buyer.get("phone") or "").strip()

        Partner = request.env["res.partner"].sudo()

        partner = False

        if email:
            partner = Partner.search([
                ("email", "=ilike", email)
            ], limit=1)

        if not partner:
            partner = Partner.search([
                ("name", "=", company_name)
            ], limit=1)

        try:
            with request.env.cr.savepoint():

                if not partner:
                    partner = Partner.create({
                        "name": company_name,
                        "email": email or False,
                        "phone": phone or False,
                        "company_type": "company",
                        "customer_rank": 1,
                    })

                Product = request.env["product.product"].sudo()
                ProductTemplate = request.env["product.template"].sudo()
                SaleOrderLine = request.env["sale.order.line"].sudo()

                lines = []

                for item in items:
                    sku = str(
                        item.get("sku")
                        or (
                            f"B2B-{item.get('product_id')}"
                            if item.get("product_id")
                            else ""
                        )
                    ).strip()

                    name = str(
                        item.get("name")
                        or sku
                        or "B2B Product"
                    ).strip()

                    qty = float(item.get("quantity") or 0)
                    price = float(item.get("price") or 0)

                    if qty <= 0:
                        return self._response({
                            "status": "error",
                            "message": f"Invalid quantity for {name}",
                        }, 422)

                    product = False

                    if sku:
                        product = Product.search([
                            ("default_code", "=", sku)
                        ], limit=1)

                    if not product:
                        template = ProductTemplate.create({
                            "name": name,
                            "default_code": sku or False,
                            "list_price": price,
                            "sale_ok": True,
                            "purchase_ok": False,
                        })

                        product = template.product_variant_id

                    line_values = {
                        "product_id": product.id,
                        "name": name,
                        "product_uom_qty": qty,
                        "price_unit": price,
                    }

                    # Odoo version-safe UoM handling.
                    if "product_uom_id" in SaleOrderLine._fields:
                        line_values["product_uom_id"] = product.uom_id.id
                    elif "product_uom" in SaleOrderLine._fields:
                        line_values["product_uom"] = product.uom_id.id

                    # Imported B2B price is treated as the supplied line price.
                    if "tax_id" in SaleOrderLine._fields:
                        line_values["tax_id"] = [(5, 0, 0)]

                    lines.append((0, 0, line_values))

                order = SaleOrder.create({
                    "partner_id": partner.id,
                    "client_order_ref": external_reference,
                    "origin": "NextGen B2B Store",
                    "note": (
                        "Imported from NextGen B2B Store.\n"
                        f"B2B Order: {order_number}"
                    ),
                    "order_line": lines,
                })

                return self._response({
                    "status": "ok",
                    "result": "created",
                    "sale_order_id": order.id,
                    "sale_order": order.name,
                    "state": order.state,
                    "external_reference": external_reference,
                    "amount_total": order.amount_total,
                    "currency": order.currency_id.name,
                }, 201)

        except Exception as exc:
            _logger.exception(
                "NextGen B2B order import failed: %s",
                order_number,
            )

            return self._response({
                "status": "error",
                "message": "OneSuite order import failed",
                "detail": str(exc),
            }, 500)
