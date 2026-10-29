/** @odoo-module **/

const PRODUCT = "OneSuite";
const COMPANY = "NextGen Technology Limited";

function createBrand() {

    const navbar =
        document.querySelector(
            ".o_main_navbar"
        );

    if (!navbar) {
        return;
    }

    if (
        navbar.querySelector(
            ".os-suite-brand"
        )
    ) {
        return;
    }

    const brand =
        document.createElement("a");

    brand.className =
        "os-suite-brand";

    brand.href =
        "/onesuite";

    brand.setAttribute(
        "aria-label",
        "OneSuite by NextGen Technology Limited"
    );

    brand.innerHTML = `
        <span class="os-suite-brand__mark"></span>

        <span class="os-suite-brand__copy">

            <span class="os-suite-brand__title">
                OneSuite
            </span>

            <span class="os-suite-brand__company">
                NextGen Technology
            </span>

        </span>
    `;

    navbar.prepend(brand);
}


function applyOneSuiteUI() {

    if (document.body) {

        document.body.classList.add(
            "os-onesuite-ui"
        );

    }

    document.title =
        `${PRODUCT} | ${COMPANY}`;

    createBrand();
}


document.addEventListener(
    "DOMContentLoaded",
    applyOneSuiteUI
);


const observer =
    new MutationObserver(
        applyOneSuiteUI
    );


observer.observe(
    document.documentElement,
    {
        subtree: true,
        childList: true,
    }
);


applyOneSuiteUI();

