from odoo import models, fields

class OperationProject(models.Model):
    _name = 'operation.project'
    _description = 'Project Management for Contractual Agreements'

    name = fields.Char(string="Project Name", required=True)
    client_id = fields.Many2one('res.partner', string="Client", required=True)
    contract_start_date = fields.Date(string="Contract Start Date", required=True)
    contract_end_date = fields.Date(string="Contract End Date", required=True)
    modality = fields.Selection([('piece_rate', 'Piece Rate'), ('whole', 'Whole'), ('defined_manpower', 'Defined Manpower')], string="Modality", required=True)
    manpower_count = fields.Integer(string="Number of Manpower", required=True)
    renewal_date = fields.Date(string="Renewal Date")
    region = fields.Char(string="Region")
    location_id = fields.Many2one('operation.location', string="Location", required=True)
    admin_cost = fields.Float(string="Administration Cost", required=True)
    fixed_rate_cost = fields.Float(string="Fixed Rate Cost", required=True)
    profit_margin_percentage = fields.Float(string="Profit Margin Percentage", required=True)
    service_type = fields.Selection([('cleaning', 'Cleaning'), ('security', 'Security')], string="Type", required=True)
    agreement_document = fields.Binary(string="Agreement Document")
   
    pension_tax_center = fields.Many2one('operation.tax.center', string="Pension Tax Center")
    income_tax_center = fields.Many2one('operation.tax.center', string="Income Tax Center")
