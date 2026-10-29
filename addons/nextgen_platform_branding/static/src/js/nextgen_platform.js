/** @odoo-module **/

const PRODUCT_NAME = "OneSuite";
const COMPANY_NAME = "NextGen Technology Limited";

function toOneSuiteUrl(value) {
    if (!value) {
        return value;
    }

    try {
        const url = new URL(value, window.location.origin);

        if (url.origin !== window.location.origin) {
            return value;
        }

        if (url.pathname === "/odoo") {
            url.pathname = "/onesuite";
        } else if (url.pathname.startsWith("/odoo/")) {
            url.pathname =
                "/onesuite/" +
                url.pathname.substring("/odoo/".length);
        }

        return url.pathname + url.search + url.hash;
    } catch (e) {
        return value;
    }
}

function fixCurrentUrl() {
    if (window.location.pathname === "/odoo") {
        history.replaceState(
            history.state,
            "",
            "/onesuite" +
                window.location.search +
                window.location.hash
        );
        return;
    }

    if (window.location.pathname.startsWith("/odoo/")) {
        history.replaceState(
            history.state,
            "",
            "/onesuite/" +
                window.location.pathname.substring("/odoo/".length) +
                window.location.search +
                window.location.hash
        );
    }
}

function fixVisibleBranding() {
    document.title =
        PRODUCT_NAME + " | " + COMPANY_NAME;

    document
        .querySelectorAll('a[href^="/odoo"]')
        .forEach((link) => {
            link.setAttribute(
                "href",
                toOneSuiteUrl(link.getAttribute("href"))
            );
        });
}

/*
 * Odoo's SPA router normally writes /odoo/... into browser history.
 * Keep its internal behavior but rewrite the browser-visible route
 * to /onesuite/... .
 */
const originalPushState =
    window.history.pushState.bind(window.history);

const originalReplaceState =
    window.history.replaceState.bind(window.history);

window.history.pushState = function (
    state,
    unused,
    url
) {
    return originalPushState(
        state,
        unused,
        toOneSuiteUrl(url)
    );
};

window.history.replaceState = function (
    state,
    unused,
    url
) {
    return originalReplaceState(
        state,
        unused,
        toOneSuiteUrl(url)
    );
};

function applyOneSuiteBranding() {
    fixCurrentUrl();
    fixVisibleBranding();
}

document.addEventListener(
    "DOMContentLoaded",
    applyOneSuiteBranding
);

window.addEventListener(
    "popstate",
    applyOneSuiteBranding
);

const observer = new MutationObserver(
    applyOneSuiteBranding
);

observer.observe(
    document.documentElement,
    {
        childList: true,
        subtree: true,
    }
);

applyOneSuiteBranding();
