/** @odoo-module **/
import { registry } from "@web/core/registry";
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

registry.category("user_menuitems").remove("odoo_account");

function auskalizeUrl(url) {
    if (typeof url !== "string") return url;
    try {
        const nextUrl = new URL(url, window.location.href);
        if (nextUrl.origin === window.location.origin && /^\/odoo(?:\/|$)/.test(nextUrl.pathname)) {
            nextUrl.pathname = nextUrl.pathname.replace(/^\/odoo(?=\/|$)/, "/auskal");
            return nextUrl.href;
        }
    } catch {}
    return url;
}

for (const method of ["pushState", "replaceState"]) {
    const original = history[method];
    history[method] = function (state, title, url) {
        return original.call(this, state, title, auskalizeUrl(url));
    };
}

function replaceLegacyPath() {
    if (/^\/odoo(?:\/|$)/.test(window.location.pathname)) {
        history.replaceState(history.state, "", auskalizeUrl(window.location.href));
    }
}
replaceLegacyPath();
window.addEventListener("popstate", replaceLegacyPath);
