# -*- coding: utf-8 -*-

from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, fields_list):
        res = super(ProductTemplate, self).default_get(fields_list)
        stock_location_ids = self.env['stock.location.route'].search([('product_selectable', '=', True), ('default_routes', '=', True)])
        if stock_location_ids:
            res['route_ids'] = [(6, 0, stock_location_ids.ids)] or []
        return res
