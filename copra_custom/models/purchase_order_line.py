from odoo import api, models, fields


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    tag = fields.Text("TAG")
    sfi = fields.Text("SFI")

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        res = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        if res.get('purchase_line_id', False):
            res['tag'] = self.tag
            res['sfi'] = self.sfi
        return res
