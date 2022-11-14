# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.depends('order_line.price_total', 'currency_id', 'amount_untaxed', 'amount_tax', 'amount_total')
    def _amount_all(self):
        _logger.warning("_amount_all_inherit" * 100)
        res = super()._amount_all()
        for order in self:
            company = self.env.company.id
            date = order.date_order
            order_currency = order.currency_id
            company_currency = self.env.company.currency_id.id
            order.update(
                {
                    'amount_untaxed_company_currency': order.currency_id._convert(order.amount_untaxed,
                                                                                  self.env.company.currency_id,
                                                                                  self.env.company, order.date_order),
                    'amount_tax_company_currency': order.currency_id._convert(order.amount_tax,
                                                                              self.env.company.currency_id,
                                                                              self.env.company, order.date_order),
                    'amount_total_company_currency': order.currency_id._convert(order.amount_total,
                                                                                self.env.company.currency_id,
                                                                                self.env.company, order.date_order),
                }
            )

        return res

    amount_untaxed_company_currency = fields.Monetary(string='Excl. Tax', store=True,
                                                      readonly=True, compute='_amount_all', tracking=True)
    amount_tax_company_currency = fields.Monetary(string='Taxes', store=True, readonly=True,
                                                  compute='_amount_all')
    amount_total_company_currency = fields.Monetary(string='Total', store=True, readonly=True,
                                                    compute='_amount_all')
    company_currency_id = fields.Many2one('res.currency', 'Company Currency', readonly=True,
                                          default=lambda self: self.env.company.currency_id.id)

