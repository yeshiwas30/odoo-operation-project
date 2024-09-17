from odoo import models, fields

class OperationEmployeeRate(models.Model):
    _name = 'operation.employee.rate'
    _description = 'Employee Rates for Project'

    project_id = fields.Many2one('operation.project', string="Project", required=True)
    rate = fields.Float(string="Employee Rate", required=True)
