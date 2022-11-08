# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def _prepare_purchase_order_line_from_procurement(
        self, product_id, product_qty, product_uom, company_id, values, po
    ):
        res = super()._prepare_purchase_order_line_from_procurement(
            product_id, product_qty, product_uom, company_id, values, po
        )
        if "sale_line_id" in values:
            line_id = self.env['sale.order.line'].search([('id', '=', values.get('sale_line_id', False))])
            if line_id and line_id.order_id.project_id:
                if line_id and line_id.order_id.project_id and line_id.order_id.project_id.account_analytic_id:
                    res.update(
                        {"account_analytic_id": line_id.order_id.project_id.account_analytic_id.id}
                    )
            else:
                if line_id and line_id.order_id.analytic_account_id:
                    res.update(
                        {"account_analytic_id": line_id.order_id.analytic_account_id.id}
                    )
        return res