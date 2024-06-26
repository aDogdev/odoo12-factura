# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomInvoice(models.Model):
    _inherit = 'account.invoice'
    _description = 'Invoice'

    user_validated = fields.Many2one('res.users', readonly=True, string='User who validated')
    
    type_invoice = fields.Selection([('rectificative','Rectificative'),('original','Original')], compute='_compute_type_invoice')

    @api.depends('refund_invoice_id')
    def _compute_type_invoice(self):
        for invoice in self:
            if bool(invoice.refund_invoice_id):
                invoice.type_invoice = "rectificative"
            else: 
                invoice.type_invoice = "original"

    @api.multi
    def invoice_validate(self):
        res = super().invoice_validate()            
        self.write({"user_validated": self.env.user.id}) 
        return res