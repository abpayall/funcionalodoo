# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    #tag_ids = fields.Many2one('helpdesk.tag', string='Helpdesk Team', default=_default_team_id, index=True)

    canal_type = fields.Many2one('res.canales', string='Canal', index=True)
    clasificacion_ticket = fields.Many2one('clasificacion.ticket', string='Clasificación', index=True)