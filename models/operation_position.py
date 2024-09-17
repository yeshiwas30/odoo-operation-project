from odoo import models, fields

class OperationPosition(models.Model):
    _name = 'operation.position'
    _description = 'Employee Position'

    name = fields.Char(string="Position Name", required=True)
    location_id = fields.Many2one('operation.location', string="Location", required=True)
    # Remove employee_ids field if you don't need it
    employee_rate = fields.Float(string="Employee Rate")
    edomias_rate = fields.Float(string="Edomias Rate")
    default_allowance = fields.Float(string="Default Allowance")
    default_transport_allowance = fields.Float(string="Default Transport Allowance")
    other_benefits = fields.Text(string="Other Benefits")