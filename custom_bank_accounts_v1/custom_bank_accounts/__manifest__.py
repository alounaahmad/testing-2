{
    'name': 'Custom Bank Accounts',
    'version': '1.0',
    'summary': 'Manage custom bank accounts and link them to contacts',
    'category': 'Accounting',
    'author': 'SSD4ME',
    'website': 'SSD4ME',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/bank_account_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
