from urllib.parse import urlencode

from odoo import http
from odoo.http import request


class OneSuiteAuthentication(http.Controller):

    @staticmethod
    def _redirect(path, params=None):

        query = dict(params or {})

        if query:
            path += "?" + urlencode(query)

        return request.redirect(
            path,
            303,
        )


    @http.route(
        "/login",
        type="http",
        auth="none",
        methods=["GET"],
        website=False,
        sitemap=False,
        csrf=False,
    )
    def login(self, **kwargs):

        params = request.httprequest.args.to_dict(
            flat=True
        )

        # After successful login enter the ERP web client.
        params.setdefault(
            "redirect",
            "/web"
        )

        return self._redirect(
            "/web/login",
            params,
        )


    @http.route(
        [
            "/register",
            "/signup",
        ],
        type="http",
        auth="none",
        methods=["GET"],
        website=False,
        sitemap=False,
        csrf=False,
    )
    def register(self, **kwargs):

        return self._redirect(
            "/web/signup",
            request.httprequest.args.to_dict(
                flat=True
            ),
        )


    @http.route(
        [
            "/forgot-password",
            "/reset-password",
        ],
        type="http",
        auth="none",
        methods=["GET"],
        website=False,
        sitemap=False,
        csrf=False,
    )
    def forgot_password(self, **kwargs):

        return self._redirect(
            "/web/reset_password",
            request.httprequest.args.to_dict(
                flat=True
            ),
        )
