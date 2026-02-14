/** @odoo-module **/

import { Component, onMounted, onWillUnmount, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class HomeMenu extends Component {
    static template = "home_menu.HomeMenu";
    static props = { action: { type: Object, optional: true }, "*": true };

    setup() {
        this.menuService = useService("menu");
        this.actionService = useService("action");
        this.state = useState({
            searchText: "",
        });

        // Toggle body class to hide navbar elements when home menu is active
        onMounted(() => {
            document.body.classList.add("o_home_menu_active");
        });
        onWillUnmount(() => {
            document.body.classList.remove("o_home_menu_active");
        });
    }

    get apps() {
        const apps = this.menuService.getApps();
        if (this.state.searchText) {
            const search = this.state.searchText.toLowerCase();
            return apps.filter((app) =>
                app.name.toLowerCase().includes(search)
            );
        }
        return apps;
    }

    onSearchInput(ev) {
        this.state.searchText = ev.target.value;
    }

    onSearchKeydown(ev) {
        if (ev.key === "Escape") {
            this.state.searchText = "";
            ev.target.value = "";
        }
        if (ev.key === "Enter") {
            const apps = this.apps;
            if (apps.length === 1) {
                this.onAppClick(apps[0]);
            }
        }
    }

    async onAppClick(app) {
        await this.menuService.selectMenu(app);
    }
}

registry.category("actions").add("home_menu", HomeMenu);
