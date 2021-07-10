# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Auto Install Modules',
    'version' : '1.0',
    'author':'Craftsync Technologies',
    'category': 'Sales',
    'maintainer': 'Craftsync Technologies',
    'description': """When you install this module it can directly install sale,purchase,accounting,Inventory modules.""",
    'summary': """Enable Auto Install modules like Sales Purchase and accounting Inventory """,

    'website': 'https://www.craftsync.com/',
    'license': 'LGPL-3',
    'support':'info@craftsync.com',
    'depends' : ['purchase','sale_stock','account','sale_management'],
    'data': [
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screen.png'],

}
