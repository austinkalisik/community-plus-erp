/** @odoo-module **/

function applyOneSuiteAuthenticationBranding() {

    const path = window.location.pathname;

    const isAuthPage =
        path === "/web/login" ||
        path === "/web/signup" ||
        path === "/web/reset_password";

    if (!isAuthPage) {
        return;
    }


    /* Browser tab */

    document.title =
        "OneSuite | NextGen Technology Limited";


    /* Keep native footer structure, change only visible text */

    document
        .querySelectorAll(
            'a[href*="odoo.com"]'
        )
        .forEach((link) => {

            link.removeAttribute(
                "href"
            );

            link.removeAttribute(
                "target"
            );

            link.textContent =
                "OneSuite by NextGen Technology Limited";
        });
}


document.addEventListener(
    "DOMContentLoaded",
    applyOneSuiteAuthenticationBranding
);


applyOneSuiteAuthenticationBranding();

