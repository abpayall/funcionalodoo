# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    #tag_ids = fields.Many2one('helpdesk.tag', string='Helpdesk Team', default=_default_team_id, index=True)

    canal_type = fields.Many2one('res.canales', string='Canal', index=True)
    clasificacion_ticket = fields.Many2one('clasificacion.ticket', string='Clasificación', index=True)
    
    

 #   @api.depends('partner_id')
 #   def _filtro_emails(self):
# for ticket in self:
            #if ticket.partner_id:
             #   ticket.partner_id.email =

    @api.depends('partner_id')
    def _get_correos_ticket(self):
        for ticket in self:
            correos_users = self.env['res.partner'].search([()])
            for correos in correos_users:
                if ticket.partner_email != correos:
                    print('Proceso Stop')
                    #correos_ticket = self.env['helpdesk.ticket'].search([('partner_email', '=', correos.email)])