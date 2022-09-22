from odoo import api, models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    height = fields.Float("Height(mm)")
    width = fields.Float("Width(mm)")
    depth = fields.Float("Depth(mm)")
    package_measurement = fields.Float("Package Measurement")
    gross_weight = fields.Float("Gross Weight(g)", digits='Stock Weight')
    net_weight = fields.Float("Net Weight(g)", digits='Stock Weight')

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
    package_measurement = fields.Float("Package Measurement", compute='_compute_package_measurement', inverse='_set_package_measurement',
                                 store=True)
    gross_weight = fields.Float("Gross Weight(g)", compute='_compute_gross_weight', inverse='_set_gross_weight',
                                 store=True, digits='Stock Weight')
    net_weight = fields.Float("Net Weight(g)",compute='_compute_net_weight', inverse='_set_net_weight',
                                 store=True, digits='Stock Weight')


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


    @api.depends('product_variant_ids', 'product_variant_ids.package_measurement')
    def _compute_package_measurement(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.package_measurement = template.product_variant_ids.package_measurement
        for template in (self - unique_variants):
            template.package_measurement = False

    def _set_package_measurement(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.package_measurement = template.package_measurement


    @api.depends('product_variant_ids', 'product_variant_ids.gross_weight')
    def _compute_gross_weight(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.gross_weight = template.product_variant_ids.gross_weight
        for template in (self - unique_variants):
            template.gross_weight = False

    def _set_gross_weight(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.gross_weight = template.gross_weight


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
