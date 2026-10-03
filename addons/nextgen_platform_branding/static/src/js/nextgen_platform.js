/** @odoo-module **/

const NEXTGEN_TITLE = "NextGen Platform";

function applyNextGenBranding() {
    const current = document.title || "";

    if (
        current.toLowerCase().includes("odoo") ||
        current.trim() === ""
    ) {
        document.title = NEXTGEN_TITLE;
    }
}

document.addEventListener(
    "DOMContentLoaded",
    applyNextGenBranding
);

const observer = new MutationObserver(
    applyNextGenBranding
);

observer.observe(
    document.documentElement,
    {
        subtree: true,
        childList: true,
    }
);
