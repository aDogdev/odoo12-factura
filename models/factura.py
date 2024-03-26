# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Factura(models.Model):
    _inherit = 'account.invoice'
    _description = 'Factura'

    user_validated = fields.Many2one('res.users', readonly=True, string='Usuario que validó')

    @api.multi
    def invoice_validate(self):
        for invoice in self:
            if invoice.partner_id not in invoice.message_partner_ids:
                invoice.message_subscribe([invoice.partner_id.id])

            # Almacenar el usuario actual
            invoice.user_validated = self.env.user

            # Auto-compute reference, if not already existing and if configured on company
            if not invoice.reference and invoice.type == 'out_invoice':
                invoice.reference = invoice._get_computed_reference()

            # DO NOT FORWARD-PORT.
            # The reference is copied after the move creation because we need the move to get the invoice number but
            # we need the invoice number to get the reference.
            invoice.move_id.ref = invoice.reference
        self._check_duplicate_supplier_reference()

        return self.write({'state': 'open'})