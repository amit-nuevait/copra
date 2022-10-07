from odoo import api, models, fields, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    height = fields.Float("Height(mm)")
    width = fields.Float("Width(mm)")
    depth = fields.Float("Depth(mm)")
    net_weight = fields.Float("Net Weight(g)", digits='Stock Weight')
    package_height = fields.Float("Package Height(mm)")
    package_width = fields.Float("Package Width(mm)")
    package_depth = fields.Float("Package Depth(mm)")
    volume = fields.Float(readonly=True, compute="compute_volume")

    @api.depends('package_height','package_width','package_depth')
    def compute_volume(self):
        for rec in self:
            rec.volume = 0.0
            if rec.package_height and rec.package_width and rec.package_depth:
                rec.volume = (rec.package_height * rec.package_width * rec.package_depth) / 1000000000

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


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    height = fields.Float("Height(mm)", compute='_compute_height', inverse='_set_height', store=True)
    width = fields.Float("Width(mm)", compute='_compute_width', inverse='_set_width', store=True)
    depth = fields.Float("Depth(mm)", compute='_compute_depth', inverse='_set_depth', store=True)
    net_weight = fields.Float("Net Weight(g)",compute='_compute_net_weight', inverse='_set_net_weight',
                                 store=True, digits='Stock Weight')
    package_height = fields.Float("Package Height(mm)", compute='_compute_package_height', inverse='_set_package_height', store=True)
    package_width = fields.Float("Package Width(mm)", compute='_compute_package_width', inverse='_set_package_width', store=True)
    package_depth = fields.Float("Package Depth(mm)", compute='_compute_package_depth', inverse='_set_package_depth', store=True)
    volume = fields.Float(readonly=True, store=True)
    
    @api.onchange('package_height','package_width','package_depth')
    def _onchange_volume(self):
        for rec in self:
            rec.volume = 0.0
            if rec.package_height and rec.package_width and rec.package_depth:
                rec.volume = (rec.package_height * rec.package_width * rec.package_depth) / 1000000000

    # height
    @api.depends('product_variant_ids', 'product_variant_ids.height')
    def _compute_height(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.height = template.product_variant_ids.height
        for template in (self - unique_variants):
            template.height = False

    def _set_height(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.height = template.height

    #width
    @api.depends('product_variant_ids', 'product_variant_ids.width')
    def _compute_width(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.width = template.product_variant_ids.width
        for template in (self - unique_variants):
            template.width = False

    def _set_width(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.width = template.width

    # depth
    @api.depends('product_variant_ids', 'product_variant_ids.depth')
    def _compute_depth(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.depth = template.product_variant_ids.depth
        for template in (self - unique_variants):
            template.depth = False

    def _set_depth(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.depth = template.depth

    # net weight
    @api.depends('product_variant_ids', 'product_variant_ids.net_weight')
    def _compute_net_weight(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.net_weight = template.product_variant_ids.net_weight
        for template in (self - unique_variants):
            template.net_weight = False

    def _set_net_weight(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.net_weight = template.net_weight

    # package height
    @api.depends('product_variant_ids', 'product_variant_ids.package_height')
    def _compute_package_height(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.package_height = template.product_variant_ids.package_height
        for template in (self - unique_variants):
            template.package_height = False

    def _set_package_height(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.package_height = template.package_height

    # package width
    @api.depends('product_variant_ids', 'product_variant_ids.package_width')
    def _compute_package_width(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.package_width = template.product_variant_ids.package_width
        for template in (self - unique_variants):
            template.package_width = False

    def _set_package_width(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.package_width = template.package_width

    # package depth
    @api.depends('product_variant_ids', 'product_variant_ids.package_depth')
    def _compute_package_depth(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.package_depth = template.product_variant_ids.package_depth
        for template in (self - unique_variants):
            template.package_depth = False

    def _set_package_depth(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.package_depth = template.package_depth

