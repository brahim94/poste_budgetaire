# -*- coding: utf-8 -*-
# from odoo import http


# class PosteBudegtaires(http.Controller):
#     @http.route('/poste_budegtaires/poste_budegtaires/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/poste_budegtaires/poste_budegtaires/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('poste_budegtaires.listing', {
#             'root': '/poste_budegtaires/poste_budegtaires',
#             'objects': http.request.env['poste_budegtaires.poste_budegtaires'].search([]),
#         })

#     @http.route('/poste_budegtaires/poste_budegtaires/objects/<model("poste_budegtaires.poste_budegtaires"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('poste_budegtaires.object', {
#             'object': obj
#         })
