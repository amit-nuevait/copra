# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    document_ids = fields.Many2many('ir.attachment',string="Documents") # ,domain="[('mimetype', 'not in', ('application/javascript','text/css'))]"