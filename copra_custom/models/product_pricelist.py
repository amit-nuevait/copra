from odoo import api, models, fields


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    discount_policy = fields.Selection(default='without_discount')
