# -*- coding: utf-8 -*-
{ 
    'name': 'Theme Grupo Mitzu', 
    'summary': 'Colores de grupo mitzu',
    'description': 'Personalización de Odoo pra las tiendas de electrónica MITZU', 
    'category': 'Tools',
    'author': 'Josué Flores Osorio', 
    'depends': ['web'], 
    'version': '1.0',
    'website': 'www.skills-depot.com',
    'data': ['views/templates.xml'],
    'auto_install' : False,
    'installable':True,
    'application':True,
    "certificate": False,
	'complexity': 'easy',
    'css': [ '/theme/static/src/css/style.scss' ],
	'js': [ ]
}