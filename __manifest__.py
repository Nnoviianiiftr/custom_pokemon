# -*- coding: utf-8 -*-
{
    'name': "custom_poke",
    'summary': "Custom Pokemon",
    'description': """Long description of module's purpose""",
    'author': "Noviani Fitri",
    'website': "https://odoo.narloci.my.id/",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    'images': ['static/description/icon.png'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/pokemon.xml',
    ],

    'installable': True,
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png']
}