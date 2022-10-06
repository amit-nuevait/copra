# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Nueva Product Website Documents',
    'version': '15.0.0.1',
    'license': 'LGPL-3',
    'category': 'website',
    'sequence': 15,
    'summary': 'Import Documents In Products',
    'description': """Import Documents In Products""",
    'author': 'NUEVA IT AS',
    'website': 'https://www.nuevait.no/',
    'maintainer': 'NUEVA IT AS',
    'depends': ['website_sale','stock','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'wizard/import_document_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
