from odoo import api, models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        if 'default_code' not in vals or not vals.get('default_code', False):
            vals['default_code'] = self.env["ir.sequence"].next_by_code('product.template.internal.ref') or _(' ')
        return super(ProductProduct, self).create(vals)

    def copy(self, default=None):
        if default is None:
            default = {}
        if self.default_code:
            default.update({
                'default_code': False,
            })
        return super(ProductProduct, self).copy(default)