from odoo import http
from odoo.http import request


class OneSuiteAlias(http.Controller):

    @http.route(
        [
            "/onesuite",
            "/onesuite/",
        ],
        type="http",
        auth="none",
        website=False,
        sitemap=False,
    )
    def onesuite(self, **kwargs):

        return request.redirect(
            "/odoo",
            303,
        )
