# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'Purchase: Default IncoTerms',
    'version': '14.0.0.0.3',
    'category': 'Inventory',
    'summary': 'Provide Sale Order Reference on Purchase Order Drop shipment.',
    'description': """
    
    """,
    #'sequence': '1',
    'author': 'ICTSTUDIO | André Schenkels',
    'website': 'http://www.ictstudio.eu',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'LGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-purchase',
    # Any module necessary for this one to work correctly
    
    'depends': ['purchase_stock'],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
