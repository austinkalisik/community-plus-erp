{
    "name": "AUSKAL OneSuite Interface",

    "version": "19.0.6.0.0",

    "summary": "AUSKAL OneSuite presentation",

    "author": "NextGen Technology Limited",

    "website": "https://nextgenpng.net",

    "license": "LGPL-3",

    "depends": [
        "web",
        "nextgen_systems_hub",
        "nextgen_platform_branding",
    ],

    # IMPORTANT:
    #
    # Native Odoo 19 web client is now used.
    #
    # No router replacement.
    # No custom OWL shell.
    # No backend SCSS.
    # No custom JS.
    # No web_responsive dependency.
    #
    "data": [],

    "assets": {
        "web.assets_backend": [
            "nextgen_onesuite_ui/static/src/js/auskal_brand.js",
            "nextgen_onesuite_ui/static/src/scss/auskal_brand.scss",
        ],
    },

    "installable": True,

    "application": False,

    "auto_install": False,
}
