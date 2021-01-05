# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NewModule(models.Model):
    _inherit = 'res.company'

    logo_1 = fields.Binary(string="Logo adicional n°1",  )
