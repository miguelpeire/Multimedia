# -*- coding: utf-8 -*-
{
    'name': "Modulo multimedia",

    'summary': """Peliculas libros generos""",

    'description': """
        Server fabricado para pruebas con Odoo 12 para el examen sobre multimedia
    """,

    'author': "DyM",
    'website': "http://www.dym.pt",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','baseModule'],

    # always loaded
    'data': [
         #'security/security.xml',
         'security/ir.model.access.csv',
     #   'templates.xml',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo.xml',
    #],
}
