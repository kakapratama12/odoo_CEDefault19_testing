# Copyright 2024 Custom
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Default Odoo 19 CE by Odi",
    "summary": "Enterprise-style Financial Reports for Odoo 19 Community",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "category": "Accounting",
    "author": "Odi",
    "description": """
    This module enhances MIS Reports to match Odoo Enterprise styling.
    Features:
    - Clean, modern layout (wide mode by default).
    - Enterprise-like headers (gray background, bold).
    - Distinct totals with top borders.
    - Smart Subtotal Separation: Automatically styles computed lines with a dark gray background fill for visual clarity.
    """,
    "depends": ["mis_builder", "account"],
    "data": [
        "views/mis_report_style_view.xml",
        "data/mis_report_styles_improved.xml",
        "data/mis_report_balance_sheet.xml",
        "data/mis_report_profit_loss.xml",
        "data/mis_report_cash_flow.xml",
    ],
    "installable": True,
    "application": False,
    "assets": {
        "web.assets_backend": [
            "mis_financial_reports/static/src/css/mis_report_custom.css",
            "mis_financial_reports/static/src/xml/mis_report_widget.xml",
        ],
    },
}
