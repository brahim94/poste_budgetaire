# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EgovRhMaTransferePoste(models.Model):
    _name = "transformation.poste"
    _rec_name = 'fiscalyear_tranformation_id'
    
    company_id = fields.Many2one('res.company', string="company")
    fiscalyear_tranformation_id = fields.Many2one("account.fiscal.year", "Année fiscale", required=True)
    transformation_line_ids = fields.One2many("transformation.poste.line", "transformation_id", string="Transformation en poste")

    # @api.onchange('transformation_line_ids')
    # def onchange_employee_id(self):
    #     for pack in self:
    #         for line in pack.transformation_line_ids:
    #             self.corp_id = line.employee_id.corp_id
    #             self.grade_id = line.employee_id.grade_id
    #             self.echelon_id = line.employee_id.echelon_id
    #             self.echelle_id = line.employee_id.echelle_id

class EgovRhMaTransferePoste(models.Model):
    _name = "transformation.poste.line"

    transformation_id = fields.Many2one('transformation.poste', string='Transformation')
    employee_id = fields.Many2one('hr.employee', string="Nom")
    corps_transformation_id = fields.Many2one(related='employee_id.corp_id', string="Corps")
    grade_transformation_id = fields.Many2one(related='employee_id.grade_id', string="Grade")
    echelon_transformation_id = fields.Many2one(related='employee_id.echelon_id', string="Echelon")
    echelle_transformation_id = fields.Many2one(related='employee_id.echelle_id', string="Echelle")
    unite_transformation_id = fields.Many2one(related='employee_id.department_id', string="Unité d'affectation")
    job_transformation_id = fields.Many2one(related='employee_id.job_id', string="Poste occupé")
    parent_transformation_id = fields.Many2one(related='employee_id.parent_id', string="Gestionnaire")

class EgovRhMaRecrutement(models.Model):
    _inherit = "egov_rh_ma.recrutement"

    user_id = fields.Many2one(required=False)

class EgovRhMaBesoinRecrutement(models.Model):
    _inherit = "egov_rh_ma.besoin_recrutement"

    def action_confirm(self):
        return self.write({'state': 'encours'})

    def action_validat(self):
        return self.write({'state': 'valide'})
