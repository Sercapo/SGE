# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",

    'summary': """
        Sirve para hacer una lista de tareas y llevar si seguimiento""",

    'description': """
    Lo mismo que antes pero algo mas largo porque si
    """,

    'author': "Sercapo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
