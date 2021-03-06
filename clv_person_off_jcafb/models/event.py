# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, models, fields


class Event(models.Model):
    _inherit = 'clv.event'

    person_off_ids = fields.Many2many(
        comodel_name='clv.person.off',
        relation='clv_person_off_event_rel',
        column1='event_id',
        column2='person_off_id',
        string='Persons Off'
    )
    count_persons_off = fields.Integer(
        string='Number of Persons Off',
        compute='_compute_count_persons_off',
        store=True
    )

    @api.depends('person_off_ids')
    def _compute_count_persons_off(self):
        for r in self:
            r.count_persons_off = len(r.person_off_ids)


class PersonOff(models.Model):
    _inherit = 'clv.person.off'

    event_ids = fields.Many2many(
        comodel_name='clv.event',
        relation='clv_person_off_event_rel',
        column1='person_off_id',
        column2='event_id',
        string='Events'
    )
    event_names = fields.Char(
        string='Event Names',
        compute='_compute_event_names',
        store=True
    )
    event_names_suport = fields.Char(
        string='Event Names Suport',
        compute='_compute_event_names_suport',
        store=False
    )

    @api.depends('event_ids')
    def _compute_event_names(self):
        for r in self:
            r.event_names = r.event_names_suport

    @api.multi
    def _compute_event_names_suport(self):
        for r in self:
            event_names = False
            for event in r.event_ids:
                if event_names is False:
                    event_names = event.name
                else:
                    event_names = event_names + ', ' + event.name
            r.event_names_suport = event_names
            if r.event_names != event_names:
                record = self.env['clv.person.off'].search([('id', '=', r.id)])
                record.write({'event_ids': r.event_ids})
