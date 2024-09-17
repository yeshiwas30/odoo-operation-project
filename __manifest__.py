{
    'name': 'Operation Management',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Manage projects, clients, locations, and employees for service agreements',
    'depends': ['base', 'hr', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/operation_project_views.xml',
        'views/operation_location_views.xml',
        #'views/operation_position_views.xml',
        #'views/operation_tax_center_views.xml',
       # 'views/operation_employee_views.xml',
         'views/hr_contract_views.xml',
    ],
    'installable': True,
    'application': True,
}
