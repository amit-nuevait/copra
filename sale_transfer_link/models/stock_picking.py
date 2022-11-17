from odoo import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_show_sale(self):
        self.ensure_one()
        if self.sale_id:
            self.ensure_one()
            return {
                'type': 'ir.actions.act_window',
                'name': 'Sales Order',
                'res_model': 'sale.order',
                'domain' : [('id','=',self.sale_id.id)],
                'view_mode': 'tree,form',
                'target' : 'current'
            }
