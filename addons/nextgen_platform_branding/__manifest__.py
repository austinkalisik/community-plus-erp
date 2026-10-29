{
    "name": "AUSKAL OneSuite",

    "version": "19.0.3.0.0",

    "summary": "Enterprise Business Management Platform by Nextgen Technology Limited",

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
        "data/catalog_branding.xml",
    ],

    # Public website CSS is loaded directly from website.xml.
    # Do not inject the old branding JS/CSS into Odoo bundles.
    "assets": {},

    "installable": True,

    "application": False,

    "auto_install": False,
}
