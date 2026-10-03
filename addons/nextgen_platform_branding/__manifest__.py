{
    "name": "NextGen Platform Branding",
    "version": "19.0.1.0.0",
    "summary": "NextGen Technology Limited platform branding",
    "description": """
NextGen Platform
================

White-label presentation for NextGen Technology Limited.

Provides:
* NextGen public platform homepage
* NextGen header and footer
* Company contact information
* Platform browser branding
* NextGen application links
* Removal of unnecessary upstream promotional branding

Odoo remains the internal ERP engine for compatibility and upgrades.
    """,
    "author": "NextGen Technology Limited",
    "website": "https://nextgenpng.net",
    "category": "Productivity",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "website",
        "nextgen_systems_hub",
    ],
    "data": [
        "views/website.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "nextgen_platform_branding/static/src/css/nextgen_platform.css",
            "nextgen_platform_branding/static/src/js/nextgen_platform.js",
        ],
        "web.assets_frontend": [
            "nextgen_platform_branding/static/src/css/nextgen_platform.css",
            "nextgen_platform_branding/static/src/js/nextgen_platform.js",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
