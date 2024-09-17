from odoo import models, fields, api

class HRContract(models.Model):
    _inherit = 'hr.contract'

    operation_location_id = fields.Many2one('operation.location', string="Operation Location")
    operation_position_id = fields.Many2one('operation.position', string="Operation Position")
    allowance = fields.Float(string="Allowance")
    transport_allowance = fields.Float(string="Transport Allowance")
    other_benefits = fields.Text(string="Other Benefits")

    @api.onchange('operation_position_id')
    def _onchange_operation_position(self):
        """
        Auto-fill or calculate fields based on selected operation_position_id
        """
        if self.operation_position_id:
            # Example: Set allowance and transport_allowance based on position
            self.allowance = self.operation_position_id.default_allowance
            self.transport_allowance = self.operation_position_id.default_transport_allowance
            self.other_benefits = self.operation_position_id.other_benefits

    @api.onchange('operation_location_id')
    def _onchange_operation_location(self):
        """
        Auto-fill or calculate fields based on selected operation_location_id
        """
        if self.operation_location_id:
            # Example: Set transport allowance based on location
            # Add or modify transport allowance based on location-specific rules
            # You can customize this part based on your location's requirements
            location_based_transport_allowance = 50  # This is an example value; replace with your logic
            self.transport_allowance += location_based_transport_allowance
