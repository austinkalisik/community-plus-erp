from odoo import http
from odoo.http import request


class NextGenPlatformController(http.Controller):

    @http.route(
        ["/platform", "/nextgen"],
        type="http",
        auth="user",
        website=False,
    )
    def nextgen_platform(self, **kwargs):
        return request.redirect("/odoo")
