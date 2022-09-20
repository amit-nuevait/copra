from odoo import api, models, fields


class ProductTemplate(models.Model):
	_inherit = "product.template"


	default_code = fields.Char('Internal Reference', compute='_compute_default_code', inverse='_set_default_code', store=True)


	@api.model
	def create(self,vals):
		if vals is None:
			vals = {}
		if not vals.get('default_code', False):
			vals['default_code'] = self.env["ir.sequence"].next_by_code('product.template.internal.ref') or _(' ')
		return super(ProductTemplate,self).create(vals)









