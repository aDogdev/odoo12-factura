# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Factura(models.Model):
    _inherit = 'account.invoice'
    _description = 'Factura'

    user_validated = fields.Many2one('res.users', readonly=True, string='Usuario que validó')
    
    rectification = fields.Selection([('rectificativa','Rectificativa'),('original','Original')], compute='_compute_rectification')

    @api.depends('refund_invoice_id')
    def _compute_rectification(self):
        for invoice in self:
            if bool(invoice.refund_invoice_id):
                invoice.rectification = "rectificativa"
            else: 
                invoice.rectification = "original"

    @api.multi
    def invoice_validate(self):
        res = super().invoice_validate()            
        self.write({"user_validated": self.env.user.id}) 
        return res