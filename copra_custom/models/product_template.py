from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        if vals is None:
            vals = {}
        if not vals.get('default_code', False):
            vals['default_code'] = self.env["ir.sequence"].next_by_code('product.template.internal.ref') or _(' ')
        return super(ProductTemplate, self).create(vals)

