# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'

    total_discount = fields.Float("Total Descuento")
