# models/operation_employee.py

from odoo import models, fields

class OperationEmployee(models.Model):
    _inherit = 'hr.employee'

    operation_location_id = fields.Many2one(
        'operation.location', string="Operation Location")
    operation_position_id = fields.Many2one(
        'operation.position', string="Operation Position")
