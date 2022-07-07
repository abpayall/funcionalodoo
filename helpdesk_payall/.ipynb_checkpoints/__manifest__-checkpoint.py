# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Payall Timer",

    'summary': """Summary""",

    'description': """
        description
    """,

    'author': "Payall",

    'website': 'https://payall.com.ve/',

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','helpdesk'],

    'data': [
        "security/ir.model.access.csv",
        "security/timer_security.xml",
        "views/res_timercito.xml",
        "views/helpdesk_ticket_inherit.xml",
        "views/res_canales.xml",
        "views/clasificacion_ticket.xml",
    ],
    'application': True,
    'demo': [

    ],
}