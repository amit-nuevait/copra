from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_doc_ids = fields.One2many('product.document', 'product_tmpl_id', 'Product Document', tracking=True)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_variant_doc_ids = fields.One2many('product.document', 'product_id', 'Product documents', tracking=True)
    product_all_doc_ids = fields.Many2many('product.document', string="Product Document", compute="_compute_product_all_doc_ids")

    @api.onchange('product_variant_doc_ids')
    def _compute_product_all_doc_ids(self):
        for rec in self:
            rec.product_all_doc_ids = rec.product_variant_doc_ids + rec.product_tmpl_id.product_doc_ids


class ProductDocument(models.Model):
    _name = 'product.document'
    _description = 'Product Document'

    name = fields.Char("Name")
    product_tmpl_id = fields.Many2one('product.template', 'Product Template ID')
    product_id = fields.Many2one('product.product', 'Product ID')
    doc_belongs = fields.Selection([('product', 'Product'), ('variant', 'Variant')],
        'Belongs', readonly=True, compute="_compute_doc_belongs", store=True)
    upload_doc = fields.Binary('Document')
    doc_type = fields.Char('Type', compute='get_file_type', store=True)

    @api.depends('upload_doc', 'name')
    def get_file_type(self):
        for rec in self:
            rec.doc_type = ''
            if rec.name:
                name = (rec.name).rpartition('.')
                rec.doc_type = name[-1].upper()

    @api.depends('product_id', 'product_tmpl_id')
    def _compute_doc_belongs(self):
        for rec in self:
            if rec.product_id and rec.product_id.is_product_variant:
                rec.doc_belongs = 'variant'
            else:
                rec.doc_belongs = 'product'
