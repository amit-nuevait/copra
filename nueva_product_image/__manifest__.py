# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Nueva Product Images',
    'version': '15.0.0.1',
    'license': 'LGPL-3',
    'category': 'Products',
    'summary': 'Import Images In Products And Varient',
    'description': """Import Images In Products And Varient""",
    'author': 'NUEVA IT AS',
    'website': 'https://www.nuevait.no/',
    'maintainer': 'NUEVA IT AS',
    'depends': ['product', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_image_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}