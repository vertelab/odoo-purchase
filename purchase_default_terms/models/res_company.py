# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    purchase_terms = fields.Text(string='Default Terms and Conditions', translate=True)