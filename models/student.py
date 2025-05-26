from odoo import models, fields, api
from datetime import date

class Student(models.Model):
    _name = 'internship.student'
    _description = 'University Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Full Name', required=True)
    photo = fields.Binary(string='Photo')
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    specialty = fields.Selection([
        ('computer_science', 'Computer Science'),
        ('engineering', 'Engineering'),
        ('business', 'Business Administration'),
        # Add more specialties as needed
    ], string='Specialty')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    student_code = fields.Char(string='Student Code', required=True)
    active = fields.Boolean(string='Active', default=True)
    internship_ids = fields.One2many('internship.record', 'student_id', string='Internships')
    thesis_ids = fields.One2many('thesis.project', 'student_id', string='Thesis Projects')

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birth_date:
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0