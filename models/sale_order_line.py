# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'

    total_discount = fields.Float("Total Descuento", store = True)

    @api.onchange('total_discount')
    def _onchange_total_discount(self):
        for line in self:
            if line.total_discount > 0:
                discount = 100 * ( line.price_total - line.total_discount) / line.price_total
                line.discount = discount
