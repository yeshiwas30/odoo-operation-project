from odoo import models, fields

class OperationLocation(models.Model):
    _name = 'operation.location'
    _description = 'Location for a Project'

    name = fields.Char(string="Location Name", required=True)
    branch_type = fields.Selection([
        ('main', 'Main Branch'),
        ('sub', 'Sub Branch')
    ], string="Branch Type")
    position_ids = fields.One2many('operation.position', 'location_id', string="Positions")
    project_ids = fields.One2many('operation.project', 'location_id', string="Projects")
    additional_allowance = fields.Float(string="Additional Allowance for Location")
    
    # New fields
    employee_rate = fields.Float(string="Employee Rate")
    edomias_rate = fields.Float(string="Edomias Rate")
