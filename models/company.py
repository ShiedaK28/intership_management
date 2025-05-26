from odoo import models, fields

class Company(models.Model):
    _name = 'internship.company'
    _description = 'Company for Internships'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Company Name', required=True)
    address = fields.Text(string='Address')
    rif = fields.Char(string='RIF')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    department_ids = fields.One2many('internship.company.department', 'company_id', string='Departments')
    active = fields.Boolean(string='Active', default=True)

class CompanyDepartment(models.Model):
    _name = 'internship.company.department'
    _description = 'Company Department'

    name = fields.Char(string='Department Name', required=True)
    company_id = fields.Many2one('internship.company', string='Company', required=True)