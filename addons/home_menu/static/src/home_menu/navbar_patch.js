/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(NavBar.prototype, {
    /**
     * Navigate to the full-page home menu instead of toggling dropdown.
     * This is used by the mobile sidebar "All Apps" button.
     */
    onAllAppsBtnClick() {
        this.actionService.doAction("home_menu", { clearBreadcrumbs: true });
    },

    /**
     * New method for the desktop 9-dot grid icon click.
     * Called from our template override that replaces the Dropdown.
     */
    onHomeMenuClick(ev) {
        ev.preventDefault();
        ev.stopPropagation();
        this.actionService.doAction("home_menu", { clearBreadcrumbs: true });
    },
});
