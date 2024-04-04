# -*- coding: utf-8 -*-
{
    'name': 'Invoice',
    'version': '1.0',
    'description': """ Implementation of the Accounting module to save the user who made the change to the Validated stage in the invoice object.""",
    'author': 'aDog',
    'category': 'Accounting',
    'depends': ['base', 'account', 'l10n_generic_coa'],
    "data": [
        "views/factura_views.xml",
    ],
    'application': True,
}
