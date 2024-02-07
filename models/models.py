# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_poke(models.Model):
#     _name = 'custom_poke.custom_poke'
#     _description = 'custom_poke.custom_poke'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

