from odoo import models, fields, api
from datetime import datetime

class AcademicPeriod(models.Model):
    _name = 'academic.period'
    _description = 'Academic Period'

    name = fields.Char(string='Period Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    report_delivery_date = fields.Date(string='Report Delivery Date')
    thesis_delivery_date = fields.Date(string='Thesis Delivery Date')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('closed', 'Closed')
    ], string='Status', default='draft')

    @api.model
    def check_period_dates(self):
        today = fields.Date.today()
        periods = self.search([])
        for period in periods:
            if period.start_date <= today <= period.end_date and period.state != 'active':
                period.write({'state': 'active'})
            elif today > period.end_date and period.state != 'closed':
                period.write({'state': 'closed'})
            elif today < period.start_date and period.state != 'draft':
                period.write({'state': 'draft'})