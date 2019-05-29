# -*- coding: utf-8 -*-
{
    'name': "Payroll Pakistan",

    'summary': """
       Human Resource Payroll""",

    'description': """
        Human Resource Payroll 
    """,

    'author': "Ahsan Zaheer",
    'website': "http://www.notahsan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_payroll'],
    
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
    ],

}
