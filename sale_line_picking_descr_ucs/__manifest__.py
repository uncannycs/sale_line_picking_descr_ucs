# -*- coding: utf-8 -*-
{
    "name": "Sale Lines Description Picking | Sales Order Delivery Details | Sales Order Line Details on Picking | Delivery Address Details | Sales Order Picking Enhancement",
    "support": "support@softhealer.com",
    "category": "Warehouse",
    "summary":
    "delivery address in sale order, invoice address delivery slip, customer address in quotation, manange quotation line module, sale order line description, manage sales order line odoo, invoice address in sale Odoo",
    "description": """
This module is useful to set invoice address, delivery address and customer address in delivery and set description from sale order line to picking operations.
delivery address in sale order, invoice address delivery slip, customer address in quotation, manange quotation line module, sale order line description, manage sales order line odoo, invoice address in sale app
                    """,
    "version": "19.0.3",
    "depends": ["sale_management", "stock"],
    "application": True,
    "data": [
        "views/stock_view.xml",
        "report/stock_report_templates.xml"
        ],
    "auto_install": False,
    "installable": True,
    'website': 'https://uncannycs.com',
    'author': 'Uncanny Consulting Services LLP',
    'maintainer': 'Uncanny Consulting Services LLP',
    'license': 'Other proprietary',
    "images": ['static/description/banner.gif'],
    "price": 50,
    "currency": "USD",
}
