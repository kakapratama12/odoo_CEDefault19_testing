from odoo import models, fields, api

class MisReportInstance(models.Model):
    _inherit = "mis.report.instance"

    wide_display_by_default = fields.Boolean(default=True)

    def _compute_matrix(self):
        """Override to inject currency into context for styling."""
        # Get the currency to use: report instance currency > company currency > user company currency
        currency = self.currency_id or self.query_company_ids[:1].currency_id or self.env.company.currency_id
        
        # Inject into context
        self = self.with_context(mis_report_currency_id=currency)
        
        return super(MisReportInstance, self)._compute_matrix()
