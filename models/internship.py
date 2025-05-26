from odoo import models, fields, api
from datetime import date, datetime

class InternshipRecord(models.Model):
    _name = 'internship.record'
    _description = 'Student Internship Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one('internship.student', string='Student', required=True)
    company_id = fields.Many2one('internship.company', string='Company', required=True)
    assigned_department = fields.Many2one('internship.company.department', string='Assigned Department')
    business_tutor = fields.Char(string='Business Tutor')
    business_tutor_position = fields.Char(string='Business Tutor Position')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    academic_tutor_id = fields.Many2one('internship.tutor', string='Academic Tutor')
    academic_period_id = fields.Many2one('academic.period', string='Academic Period', required=True)
    accreditation_required = fields.Boolean(string='Accreditation Required')
    accreditation_approved = fields.Boolean(string='Accreditation Approved', readonly=True)
    position = fields.Char(string='Position Held')
    experience_years = fields.Integer(string='Years of Experience in Position')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('evaluated', 'Evaluated')
    ], string='Status', default='draft')
    evaluation_notes = fields.Text(string='Evaluation Notes')
    final_report = fields.Binary(string='Final Report')
    final_report_filename = fields.Char(string='Final Report Filename')

    @api.onchange('student_id')
    def _onchange_student_id(self):
        if self.student_id:
            return {'domain': {'academic_period_id': [('state', '=', 'active')]}}

    def action_start_internship(self):
        self.write({'state': 'in_progress'})

    def action_complete_internship(self):
        self.write({'state': 'completed'})

    def action_evaluate_internship(self):
        self.write({'state': 'evaluated'})

    def action_request_accreditation(self):
        if self.accreditation_required:
            # Logic to request accreditation
            pass