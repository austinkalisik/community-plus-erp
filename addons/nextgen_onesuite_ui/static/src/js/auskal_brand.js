/** @odoo-module **/

const PRODUCT_TITLE = "AUSKAL OneSuite";
const BRAND_ICON = "/nextgen_onesuite_ui/static/src/img/auskal-mark.svg";

function applyAuskalIdentity() {
    if (document.title !== PRODUCT_TITLE) {
        document.title = PRODUCT_TITLE;
    }
    for (const link of document.querySelectorAll("link[rel~='icon']")) {
        if (link.getAttribute("href") !== BRAND_ICON) {
            link.setAttribute("href", BRAND_ICON);
        }
    }
}

applyAuskalIdentity();
new MutationObserver(applyAuskalIdentity).observe(document.documentElement, {
    subtree: true,
    childList: true,
    characterData: true,
});
