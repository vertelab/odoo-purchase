from odoo import models, fields, api, _



class Purchase(models.Model):
    _inherit = 'purchase.order'

    def order_deadline_cron_job(self):
        for order in self.env['purchase.order'].search([]):
            if order.date_order and order.date_order > fields.Datetime.today():
                print("Hello")