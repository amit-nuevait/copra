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

    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, company_id, values, po):
        res = super(PurchaseOrderLine, self)._prepare_purchase_order_line_from_procurement(product_id, product_qty, product_uom, company_id, values, po)
        if res.get('sale_line_id', False):
            sale_line_rec = self.env['sale.order.line'].browse(res['sale_line_id'])
            res['sfi'] = sale_line_rec.sfi or ''
            res['tag'] = sale_line_rec.tag or ''
        return res
