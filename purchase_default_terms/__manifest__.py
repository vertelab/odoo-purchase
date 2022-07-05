# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'Purchase Default IncoTerms',
    'version': '14.0.0.0.3',
    'category': 'Purchase Management',
    'author': 'ICTSTUDIO | André Schenkels',
    'website': 'http://www.ictstudio.eu',
    'license': 'LGPL-3',
    'summary': 'Provide Sale Order Reference on Purchase Order Dropshipment',
    'depends': [
        'purchase_stock'
    ],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
}
