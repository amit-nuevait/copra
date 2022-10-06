from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    freight_type = fields.Selection([("air", "Air"), ("sea", "Sea"), ("train", "Train"), ("road", "Road")], string="Freight Type")
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    tag = fields.Text("TAG")
    sfi = fields.Text("SFI")