# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class ResCanales(models.Model):
    _name = 'clasificacion.ticket'
    _description = 'Clasificación de los tickets'

    #tag_ids = fields.Many2one('helpdesk.tag', string='Helpdesk Team', default=_default_team_id, index=True)
    name = fields.Char(string='Clasificacion')
    clasificacion_ticket_ids = fields.One2many(string='Clasificación', comodel_name='helpdesk.ticket',
                                           inverse_name='clasificacion_ticket')


