# -*- coding: utf-8 -*-
{
    'name': 'Factura',
    'version': '1.0',
    'description': """ Implementación del módulo de Contabilidad para guardar en el objeto factura el usuario que realizó el cambio a la etapa Validado.""",
    'author': 'aDog',
    'category': 'Accounting',
    'depends': ['base', 'account', 'l10n_generic_coa'],
    "data": [
        "views/factura_views.xml",
    ],
    'application': True,
}
