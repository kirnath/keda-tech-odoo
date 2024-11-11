# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class material_custom(models.Model):
    _name = 'material.custom'
    _description = 'Material Custom'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    type = fields.Selection(
        selection=[
            ('fabric', 'Fabric'),
            ('jeans', 'Jeans'),
            ('cotton', 'Cotton'),
        ],
        string='Type',
        required=True,
    )
    buy_price = fields.Integer(required=True)
    related_supplier = fields.Many2one('res.partner', string='Supplier', required=True)

    @api.constrains('buy_price')
    def _check_minimum_value(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("The value of 'Buy Price' must be at least 100")