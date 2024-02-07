from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    custom_bank_account_ids = fields.Many2many(
        'custom.bank.account', 
        'partner_bank_rel', 
        'partner_id', 
        'bank_account_id',
        string='Custom Bank Accounts'
    )
