# -*- coding: utf-8 -*-
##################################################
#                                                #
#    Cyb3rSky Corp. (A group for freelancers)    #
#    Copyright (C) 2021 onwards                  #
#                                                #
#    Email: cybersky25@gmail.com                 #
#                                                #
##################################################

{
    'name': 'Python Library Installer',
    'version': '1.1',
    'category': 'Utility',
    "sequence": 3,
    'summary': 'Install python libraries without accessing the server CLI',
    'complexity': "easy",
    'author': 'Cyb3rSky',
    'website': 'http://cyb3rsky.co.in',
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/installer_view.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
