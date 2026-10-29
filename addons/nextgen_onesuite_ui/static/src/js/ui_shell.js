/** @odoo-module **/

const TITLE = "OneSuite | NextGen Technology Limited";

function createNavbarBrand() {
    const navbar = document.querySelector(".o_main_navbar");

    if (!navbar) {
        return;
    }

    if (navbar.querySelector(".os-navbar-brand")) {
        return;
    }

    const brand = document.createElement("a");

    brand.className = "os-navbar-brand";
    brand.href = "/onesuite";
    brand.setAttribute(
        "aria-label",
        "OneSuite by NextGen Technology Limited"
    );

    brand.innerHTML = `
        <span class="os-navbar-brand__mark"></span>
        <span class="os-navbar-brand__text">
            <span class="os-navbar-brand__name">
                OneSuite
            </span>
            <span class="os-navbar-brand__company">
                NextGen Technology
            </span>
        </span>
    `;

    navbar.prepend(brand);
}

function applyCorporateUI() {
    document.body?.classList.add(
        "os-corporate-ui"
    );

    document.title = TITLE;

    createNavbarBrand();
}

document.addEventListener(
    "DOMContentLoaded",
    applyCorporateUI
);

const observer = new MutationObserver(
    applyCorporateUI
);

observer.observe(
    document.documentElement,
    {
        childList: true,
        subtree: true,
    }
);

applyCorporateUI();
