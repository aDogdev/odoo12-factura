# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Factura(models.Model):
    _inherit = 'account.invoice'
    _description = 'Factura'

    user_validated = fields.Many2one('res.users', readonly=True, string='Usuario que validó')

    @api.multi
    def invoice_validate(self):
        res = super().invoice_validate()            
        self.write({"user_validated": self.env.user.id}) 
        return res