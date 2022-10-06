# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Acsl Project',
    'version': '15.0.0.0',
    'license': 'LGPL-3',
    'category': 'Project',
    'sequence': 15,
    'summary': 'Module for show default list view on project level',
    'description': """Module for show default list view on project level""",
    'author': 'Nueva IT AS',
    'website': 'nueva.no',
    'maintainer': 'Nueva IT AS',
    'depends': ['project'],
    'images': ['static/description/icon.png'],
    'data': [
        'views/project_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 100.0,
}
