# -*- coding: utf-8 -*-
from odoo import http

# class MethodExtraLogoCompany(http.Controller):
#     @http.route('/method_extra_logo_company/method_extra_logo_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_extra_logo_company/method_extra_logo_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_extra_logo_company.listing', {
#             'root': '/method_extra_logo_company/method_extra_logo_company',
#             'objects': http.request.env['method_extra_logo_company.method_extra_logo_company'].search([]),
#         })

#     @http.route('/method_extra_logo_company/method_extra_logo_company/objects/<model("method_extra_logo_company.method_extra_logo_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_extra_logo_company.object', {
#             'object': obj
#         })