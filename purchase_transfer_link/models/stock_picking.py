from odoo import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_show_purchase(self):
        self.ensure_one()
        if self.purchase_id:
            self.ensure_one()
            return {
                'type': 'ir.actions.act_window',
                'name': 'Purchase Order',
                'res_model': 'purchase.order',
                'domain' : [('id','=',self.purchase_id.id)],
                'view_mode': 'tree,form',
                'target' : 'current'
            }
