/** @odoo-module **/

function applyOneSuiteLogin() {
    const form =
        document.querySelector(".oe_login_form");

    if (!form) {
        return;
    }

    if (form.querySelector(".os-login-brand")) {
        return;
    }

    const brand = document.createElement("div");

    brand.className = "os-login-brand";

    brand.innerHTML = `
        <div class="os-login-brand__mark">
            NEXTGEN TECHNOLOGY LIMITED
        </div>

        <div class="os-login-brand__title">
            Welcome to OneSuite
        </div>

        <div class="os-login-brand__subtitle">
            Sign in to your business workspace.
        </div>
    `;

    form.prepend(brand);

    document.title =
        "OneSuite Login | NextGen Technology Limited";
}

document.addEventListener(
    "DOMContentLoaded",
    applyOneSuiteLogin
);

applyOneSuiteLogin();
