# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPoke(http.Controller):
#     @http.route('/custom_poke/custom_poke', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_poke/custom_poke/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_poke.listing', {
#             'root': '/custom_poke/custom_poke',
#             'objects': http.request.env['custom_poke.custom_poke'].search([]),
#         })

#     @http.route('/custom_poke/custom_poke/objects/<model("custom_poke.custom_poke"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_poke.object', {
#             'object': obj
#         })

