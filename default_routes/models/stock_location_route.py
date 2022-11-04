# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockLocationRoute(models.Model):
    _inherit = 'stock.location.route'

    default_routes = fields.Boolean(string="Default Routes")

    @api.onchange('product_selectable')
    def _change_default_routes(self):
        if self.product_selectable == False:
            self.default_routes = False