# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2017 Vertel AB (<http://vertel.se>).
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
    'name': 'Purchase Calc Pallets',
    'version': '0.1',
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'category': 'base',
    'website': 'http://www.vertel.se',
    'summary': 'Calculates pallets for a purchase order',
    'description': """
Calculates incomming volumes in pallets for a purchase order.
This is a rough estimate of the number of pallets that the
supplier will use for the delivery. This is for planning
delivery reception. We don't know if the supplier uses mixed 
pallets or not.

After installation of module:
1) Activate "Allow to define several packaging methods on products" in Settings/Configuration/Warehouse
2) On products and raw material bought: Inventory -> Packaging / Configuration and add a configuration that holds
   a Pallet Logistik unit of the type pallet. The number of units fitted on a pallet is calculated by 
   Quantity by package * Package by layer * Number of layers.
   
If there are several pallet configurations we choose the largest pallet that holds the most units of the product.
Even if a whole purchase order fits on a single pallet it will be counted as at least one pallet.


Financed by Dermanord
    """,
    'depends': ['purchase','delivery' ],
    'data': [
        'purchase_view.xml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
