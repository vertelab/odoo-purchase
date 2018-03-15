# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Purchase Cavarosa',
    'version': '0.1',
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'category': 'purchase',
    'website': 'http://www.vertel.se',
    'summary': 'Adaptions for Cavarosa',
    'description': """
Print out purchase order line tags
==================================
    """,
    'depends': ['purchase', 'report_glabels', 'sale_purchase'],
    'data': [
        'report_purchaseorder.xml',
        'purchaseorder_data.xml',
        'purchase_view.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
