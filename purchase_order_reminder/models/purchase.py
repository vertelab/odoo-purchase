from odoo import models, fields, api, _



class Purchase(models.Model):
    _inherit = 'purchase.order'

    def order_deadline_cron_job(self):
        mail_template = self.env.ref('purchase_order_reminder.email_purchase_order_deadline')
        for order in self.env['purchase.order'].search([]):
            if order.date_order and fields.Datetime.today() > order.date_order:
                mail_template.send_mail(order.id, force_send=True)