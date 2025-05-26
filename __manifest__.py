# internship_management/__manifest__.py
{
    'name': 'Internship and Thesis Management',
    'version': '1.0',
    'summary': 'Manage student internships and thesis projects',
    'description': """
        Comprehensive module for managing student internships and thesis projects.
        Features include:
        - Student registration and management
        - Tutor assignment and tracking
        - Company and department management
        - Academic period configuration
        - Internship accreditation process
        - Custom user roles with specific permissions
    """,
    'author': 'Your Name',
    'website': 'https://www.youruniversity.edu',
    'category': 'Education',
    'depends': [
        'base',
        'mail',
        'web',
    ],
    'data': [
        # Security
        'security/internship_security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/student_views.xml',
        'views/tutor_views.xml',
        'views/company_views.xml',
        'views/academic_period_views.xml',
        'views/internship_views.xml',
        
        # Data
        'data/academic_period_data.xml',
        'data/specialty_data.xml',
        
        # Menus
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/student_demo.xml',
        'demo/tutor_demo.xml',
        'demo/company_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'internship_management/static/src/css/internship_style.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'price': 0,
    'currency': 'USD',
}