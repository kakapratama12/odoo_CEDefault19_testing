# -*- coding: utf-8 -*-
{
    'name': 'Home Menu',
    'version': '19.0.1.0.0',
    'summary': 'Enterprise-style full-page home menu for Community Edition',
    'description': """
        Replaces the default app dropdown with a full-page home screen
        showing installed app tiles, similar to Odoo Enterprise Edition.
    """,
    'category': 'Tools',
    'author': 'Custom',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'home_menu/static/src/home_menu/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
