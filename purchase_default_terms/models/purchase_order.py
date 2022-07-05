# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from odoo import models, fields, api, _


_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _default_note(self):
        return self.env['ir.config_parameter'].sudo().get_param('purchase_default_terms.use_purchase_terms') and self.env.company.purchase_terms or ''

    notes = fields.Text('Terms and Conditions', default=_default_note)

    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        super().onchange_partner_id()
        if self.env['ir.config_parameter'].sudo().get_param('purchase_default_terms.use_purchase_terms') and self.env.company.purchase_terms:
            self.notes = self.with_context(lang=self.partner_id.lang).env.company.purchase_terms
        return {}