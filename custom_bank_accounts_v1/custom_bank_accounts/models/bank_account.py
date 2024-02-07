from odoo import models, fields, api

class CustomBankAccount(models.Model):
    _name = 'custom.bank.account'
    _description = 'Custom Bank Account'


    partner_id = fields.Many2one('res.partner', string='Partner')
    bank_name = fields.Char(string='Bank Name')
    bank_branch = fields.Char(string='Bank Branch')
    bank_account = fields.Char(string='Bank Account')
    iban = fields.Char(string='IBAN')
    swift_code = fields.Char(string='SWIFT Code')
    routing_code = fields.Char(string='Routing Code for WPS')
    responsible_id = fields.Many2one('res.users', string='Responsible')

    partner_count = fields.Integer(string='Number of Partners', compute='_compute_partner_count')

    def _compute_partner_count(self):
        for record in self:
            partners = self.env['res.partner'].search([('custom_bank_account_ids', 'in', record.id)])
            record.partner_count = len(partners)

    def action_view_related_partners(self):
        self.ensure_one()
        action = self.env.ref('custom_bank_accounts.action_view_partners_with_account').read()[0]
        action['domain'] = [('custom_bank_account_ids', 'in', self.id)]
        return action
