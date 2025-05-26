from odoo import models, fields

class Tutor(models.Model):
    _name = 'internship.tutor'
    _description = 'Academic Tutor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    contact_info = fields.Text(string='Contact Information')
    specialty = fields.Selection([
        ('computer_science', 'Computer Science'),
        ('engineering', 'Engineering'),
        ('business', 'Business Administration'),
        # Add more specialties as needed
    ], string='Specialty')
    assigned_students = fields.One2many('internship.record', 'academic_tutor_id', string='Assigned Students')
    active = fields.Boolean(string='Active', default=True)
    user_id = fields.Many2one('res.users', string='Related User', required=True)