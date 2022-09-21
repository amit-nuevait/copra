
{
    "name":"Copra Customization",
    "summary": "Copra Customization",
    "version":'15.0.1.0',
    "author":"Nueva IT",
    "company": "Nueva IT",
    "category": 'Sales/Sales',
    "depends": ['base', 'sale_management', 'product',
                'sale_stock'],
    "license":"LGPL-3",
    "sequence": 100,
    "data": [
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True,
    "auto_install": False,
}
