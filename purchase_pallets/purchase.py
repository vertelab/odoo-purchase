# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
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
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.tools

from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp

import math

import logging
_logger = logging.getLogger(__name__)

class purchase_order(models.Model):
    _inherit = 'purchase.order'

    @api.one
    def _calc_pallets(self):
        #raise Warning(self.order_line)
        #~ self.calc_pallets = 222
       self.calc_pallets = int(math.ceil(sum(self.order_line.mapped('calc_pallets')) + 0.0001))
    calc_pallets = fields.Integer(compute="_calc_pallets",string="Pallets")
    
    #~ calc_pallets = fields.Integer()

class purchase_order_line(models.Model):  
    _inherit = 'purchase.order.line'
    
    @api.one
    def _calc_pallets(self):
        self.calc_pallets = self.product_id.get_calc_pallets(self.product_qty)
    calc_pallets = fields.Float(compute="_calc_pallets")

class product_product(models.Model):  
    _inherit = 'product.product'
    
    @api.multi
    def get_calc_pallets(self,product_qty):
        pallets = 0.0
        pallet = self.packaging_ids.filtered(lambda p: p.ul_container.type == 'pallet').mapped('calc_pallets')
        pallet.sort()
        if pallet and pallet[-1] > 0:
            pallets = product_qty  / pallet[-1]
        return pallets

class product_packaging(models.Model):  
    _inherit = 'product.packaging'

    @api.one
    def _calc_pallets(self):
        self.calc_pallets = self.qty * self.ul_qty * self.rows
    calc_pallets = fields.Float(compute="_calc_pallets")



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: