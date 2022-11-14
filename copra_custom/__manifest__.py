
{
    "name":"Copra Customization",
    "summary": "Copra Customization",
    "version":'15.0.1.0',
    "author":"Nueva IT",
    "company": "Nueva IT",
    "category": 'Sales/Sales',
    "depends": ['base', 'sale_management', 'product',
                'sale_stock', 'purchase', 'purchase_stock',
                'stock_dropshipping', 'sale_project'],
    "license":"LGPL-3",
    "sequence": 100,
    "data": [
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "report/picking_report.xml",
        "views/sale_order_view.xml",
        "views/stock_picking_view.xml",
        "views/purchase_order_line_view.xml",
        "views/product_template_view.xml",
        "views/project_view.xml"
    ],
    "installable": True,
    "auto_install": False,
}
