# -*- coding: utf-8 -*-
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'Purchase: Controls VAT on Purchase Report',
    'version': '14.0.0.0.1',
    'category': 'Inventory/Purchase',
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-purchase/purchase_delivery_vat_report',
    'license': 'LGPL-3',
    'summary': 'Controls VAT on Purchase Report',
    'depends': [
        'base_company_fiscal_position',
        'purchase_stock'
    ],
    'data': [
        'report/purchase_report_templates.xml',
    ],
    'installable': True,
}
