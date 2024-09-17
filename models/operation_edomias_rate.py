from odoo import models, fields

class OperationEdomiasRate(models.Model):
    _name = 'operation.edomias.rate'
    _description = 'Edomias Rates for Project'

    project_id = fields.Many2one('operation.project', string="Project", required=True)
    rate = fields.Float(string="Edomias Rate", required=True)
