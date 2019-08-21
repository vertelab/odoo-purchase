# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2017- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    purchase_ids = fields.Many2many(comodel_name='purchase.order', string='Purchase Orders', compute='_compute_purchase_ids', search='_search_purchase_ids')
    purchase_count = fields.Integer(string='Purchase Count', compute='_compute_purchase_ids')
    
    @api.one
    def _compute_purchase_ids(self):
        self.purchase_ids = self.env['purchase.order'].search([('sale_ids', '=', self.id)])
        self.purchase_count = len(self.purchase_ids)
    
    @api.model
    def _search_purchase_ids(self, op, val):
        # Untested
        # ~ _logger.warn('\n\n_search_purchase_ids(%s, %s)\n' % (op, val))
        field = 'id'
        if type(val) in (list, tuple):
            for v in val:
                if isinstance(v, basestring):
                     field = 'name'
                     break
        elif isinstance(val, basestring):
            field = 'name'
        order_ids = []
        for p in self.env['purchase.order'].search_read([(field, op, val)], ['sale_ids']):
            # ~ _logger.warn(p)
            order_ids.append(p[1])
        return [('id', 'in', list(set(order_ids)))]
    
    @api.multi
    def action_view_purchases(self):
        purchases = self.mapped('purchase_ids')
        action = self.env.ref('purchase.purchase_form_action').read()[0]
        if len(purchases) > 1:
            action['domain'] = [('id', 'in', purchases.ids)]
        elif len(purchases) == 1:
            action['domain'] = []
            action['views'] = [(self.env.ref('purchase.purchase_order_form').id, 'form')]
            action['res_id'] = purchases.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
    
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    sale_id = fields.Many2one(comodel_name='sale.order', string='Sale Order')
    sale_ids = fields.Many2many(comodel_name='sale.order', string='Sale Orders', compute='_compute_sale_ids', store=True)
    
    @api.depends('order_line.procurement_ids.sale_line_id.order_id')
    @api.one
    def _compute_sale_ids(self):
        self.sale_ids = self.order_line.mapped('procurement_ids').mapped('sale_line_id').mapped('order_id')

class ProcurementOrder(models.Model):
    _inherit = "procurement.order"
    
    @api.model
    def sale_purchase_limit(self):
        """Check if we should limit a purchase order to one sale order."""
        return bool(int(self.env['ir.config_parameter'].get_param('sale_purchase_fix_relation.sale_purchase_limit', '1')))
    
    @api.multi
    def _prepare_purchase_order(self, partner):
        """Add the sale order of current procurement to sale_ids on the purchase order."""
        vals = super(ProcurementOrder, self)._prepare_purchase_order(partner)
        if self.sale_purchase_limit():
            if self.sale_line_id:
                vals['sale_id'] = self.sale_line_id.order_id.id
        return vals
    
    # Search for an existing purchase order to add this procurement to.
    # If we wish to maintain a many to 1 between sale and purchase, this would be the place to implement it.
    # We can also separate products that should be kept separate (physical / intangible) to different orders.
    def _make_po_get_domain(self, partner):
        domain = super(ProcurementOrder, self)._make_po_get_domain(partner)
        
        if self.sale_purchase_limit():
            domain = list(domain) # Tuple because it's used as key in a dict
            if self.sale_line_id:
                domain.append(('sale_id', '=', self.sale_line_id.order_id.id))
            else:
                domain.append(('sale_id', '=', False))
            domain = tuple(domain)
        return domain
    
    # Le sigh. They didn't make all the relevant parts of this inheritable, so we'll have to overwrite make_po if we want to group order lines differently.
    # Looks like it's implemented in purchase and purchase_requisition (which we aren't very interested in atm).
    # For now we can use a computed field instead.
    # ~ @api.multi
    # ~ def make_po(self):
        # ~ cache = {}
        # ~ res = []
        # ~ for procurement in self:
            # ~ suppliers = procurement.product_id.seller_ids\
                # ~ .filtered(lambda r: (not r.company_id or r.company_id == procurement.company_id) and (not r.product_id or r.product_id == procurement.product_id))
            # ~ if not suppliers:
                # ~ procurement.message_post(body=_('No vendor associated to product %s. Please set one to fix this procurement.') % (procurement.product_id.name))
                # ~ continue
            # ~ supplier = procurement._make_po_select_supplier(suppliers)
            # ~ partner = supplier.name

            # ~ domain = procurement._make_po_get_domain(partner)

            # ~ if domain in cache:
                # ~ po = cache[domain]
            # ~ else:
                # ~ po = self.env['purchase.order'].search([dom for dom in domain])
                # ~ po = po[0] if po else False
                # ~ cache[domain] = po
            # ~ if not po:
                # ~ vals = procurement._prepare_purchase_order(partner)
                # ~ po = self.env['purchase.order'].create(vals)
                # ~ name = (procurement.group_id and (procurement.group_id.name + ":") or "") + (procurement.name != "/" and procurement.name or "")
                # ~ message = _("This purchase order has been created from: <a href=# data-oe-model=procurement.order data-oe-id=%d>%s</a>") % (procurement.id, name)
                # ~ po.message_post(body=message)
                # ~ cache[domain] = po
            # ~ elif not po.origin or procurement.origin not in po.origin.split(', '):
                # ~ # Keep track of all procurements
                # ~ if po.origin:
                    # ~ if procurement.origin:
                        # ~ po.write({'origin': po.origin + ', ' + procurement.origin})
                    # ~ else:
                        # ~ po.write({'origin': po.origin})
                # ~ else:
                    # ~ po.write({'origin': procurement.origin})
                # ~ name = (self.group_id and (self.group_id.name + ":") or "") + (self.name != "/" and self.name or "")
                # ~ message = _("This purchase order has been modified from: <a href=# data-oe-model=procurement.order data-oe-id=%d>%s</a>") % (procurement.id, name)
                # ~ po.message_post(body=message)
            # ~ if po:
                # ~ res += [procurement.id]

            # ~ # Create Line
            # ~ po_line = False
            # ~ for line in po.order_line:
                # ~ if line.product_id == procurement.product_id and line.product_uom == procurement.product_id.uom_po_id:
                    # ~ procurement_uom_po_qty = procurement.product_uom._compute_quantity(procurement.product_qty, procurement.product_id.uom_po_id)
                    # ~ seller = procurement.product_id._select_seller(
                        # ~ partner_id=partner,
                        # ~ quantity=line.product_qty + procurement_uom_po_qty,
                        # ~ date=po.date_order and po.date_order[:10],
                        # ~ uom_id=procurement.product_id.uom_po_id)

                    # ~ price_unit = self.env['account.tax']._fix_tax_included_price_company(seller.price, line.product_id.supplier_taxes_id, line.taxes_id, self.company_id) if seller else 0.0
                    # ~ if price_unit and seller and po.currency_id and seller.currency_id != po.currency_id:
                        # ~ price_unit = seller.currency_id.compute(price_unit, po.currency_id)

                    # ~ po_line = line.write({
                        # ~ 'product_qty': line.product_qty + procurement_uom_po_qty,
                        # ~ 'price_unit': price_unit,
                        # ~ 'procurement_ids': [(4, procurement.id)]
                    # ~ })
                    # ~ break
            # ~ if not po_line:
                # ~ vals = procurement._prepare_purchase_order_line(po, supplier)
                # ~ self.env['purchase.order.line'].create(vals)
        # ~ return res
