{
    "name": "NextGen Systems Hub",
    "version": "19.0.1.1.0",
    "summary": "Central launcher for NextGen Technology business systems",
    "description": """
NextGen Systems Hub
===================

Central access to NextGen Technology systems.

Business Systems
----------------
* OneSuite ERP
* NexERP
* NextGen B2B Store

Infrastructure and Operations
-----------------------------
* SMS Gateway
* Paperclip
* God's Eye

The applications remain independently deployed at their live URLs.
Updates to those applications therefore become available immediately
through this hub without copying their source code into Odoo.
    """,
    "author": "NextGen Technology PNG Limited",
    "website": "https://www.nextgenpng.net",
    "category": "Productivity",
    "license": "LGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "views/nextgen_systems_menus.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
