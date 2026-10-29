from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home


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
            "/auskal/apps",
            303,
        )

class AuskalWebClient(Home):
    @http.route(
        [
            "/auskal",
            "/auskal/",
            "/auskal/<path:path>",
        ],
        type="http",
        auth="user",
        website=False,
        sitemap=False,
    )
    def auskal_web_client(self, path=None, **kwargs):
        return super().web_client(**kwargs)
