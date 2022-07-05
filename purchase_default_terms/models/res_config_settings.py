# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    purchase_terms = fields.Text(related='company_id.purchase_terms', string="Purchase Terms & Conditions", readonly=False)
    use_purchase_terms = fields.Boolean(
        string='Default Purchase Terms & Conditions',
        config_parameter='purchase_default_terms.use_purchase_terms')