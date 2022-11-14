# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Transfer Link',
    'version': '15.0.0.0',
    'license': 'LGPL-3',
    'category': 'Purchase',
    'sequence': 15,
    'summary': 'Show purchase orders related to particular receipt.',
    'description': """ """,
    'author': 'Accudoo Solutions Pvt. Ltd.',
    'website': 'https://accudoo.com',
    'maintainer': 'Accudoo Solutions Pvt. Ltd.',
    'depends': ['purchase','stock'],
    'images': ['static/description/icon.png'],
    'data': [
        'views/stock_picking_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 100.0,
    'currency': 'EUR',
}
