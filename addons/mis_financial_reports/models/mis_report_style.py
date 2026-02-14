from odoo import models, api, fields

class MisReportStyle(models.Model):
    _inherit = "mis.report.style"

    @api.model
    def render_num(
        self, lang, value, divider=1.0, dp=0, prefix=None, suffix=None, sign="-", format_type="default"
    ):
        # Dynamic Currency Logic:
        # If no specific prefix is set in the style, try to use the currency from context.
        # The currency is injected into context by our MisReportInstance override.
        if not prefix:
            currency = self.env.context.get("mis_report_currency_id")
            if currency:
                prefix = currency.symbol
                # If dp is 0 (default style), use currency precision
                if dp == 0:
                    dp = currency.decimal_places

        return super(MisReportStyle, self).render_num(
            lang, value, divider, dp, prefix, suffix, sign, format_type
        )

    css_class = fields.Char(string="CSS Class", help="Custom CSS class to apply to the report row (e.g., mis_enterprise_header)")
