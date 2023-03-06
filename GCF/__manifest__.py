# -*- coding: utf-8 -*-
{
    'name': "GCF",  # Titulo del módulo
    'summary': "Gestor de ciclos Formativos",  # Resumen de la funcionaliadad
    'description': """
    Gestiona los distintos ciclos formativos consus modulos, cada uno con Alumnos y profesores.
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "DAMB",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        
        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/GCF_centros.xml',
        'views/GCF_ciclos.xml',
        'views/GCF_modulos.xml',
        'views/GCF_alumnos.xml',
        'views/GCF_categorias.xml',
        'views/GCF_profesores.xml',
        'views/GCF_directores.xml',

    ],
}
