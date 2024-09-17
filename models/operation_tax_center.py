from odoo import models, fields

class OperationTaxCenter(models.Model):
    _name = 'operation.tax.center'
    _description = 'Tax Center Information'

    name = fields.Char(string="Tax Center Name", required=True)
    type = fields.Selection([('pension', 'Pension'), ('income', 'Income')], string="Tax Type", required=True)
