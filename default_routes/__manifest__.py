# -*- coding: utf-8 -*-
{
    'name': "Default Routes on Products",

    'summary': """Set default routes while creating new product""",

    'description': """Set default routes while creating new product""",

    'author': "Nueva IT AS",
    'website': "https://www.nuevait.no",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'views/stock_location_route.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
