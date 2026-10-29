/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class OneSuiteDashboard extends Component {
    static template =
        "nextgen_onesuite_ui.OneSuiteDashboard";
}

registry
    .category("actions")
    .add(
        "nextgen_onesuite_dashboard",
        OneSuiteDashboard
    );
