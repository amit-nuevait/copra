from odoo import api, models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    tag = fields.Text("TAG")
    sfi = fields.Text("SFI")

    def _prepare_procurement_values(self):
        res = super(StockMove, self)._prepare_procurement_values()
        if self.sale_line_id:
            res['tag'] = self.sale_line_id.tag
            res['sfi'] = self.sale_line_id.sfi
        return res
        

class StockRule(models.Model):

    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        res = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        if res.get('sale_line_id', False):
            sale_line_rec = self.env['sale.order.line'].browse(res['sale_line_id'])
            res['tag'] = sale_line_rec.tag
            res['sfi'] = sale_line_rec.sfi
        return res
