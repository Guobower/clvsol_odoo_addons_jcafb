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

import logging

from odoo import api, fields, models
from odoo import exceptions

_logger = logging.getLogger(__name__)


class AnimalMngAddressConfirm(models.TransientModel):
    _name = 'clv.animal.mng.address_confirm'

    def _default_animal_mng_ids(self):
        return self._context.get('active_ids')
    animal_mng_ids = fields.Many2many(
        comodel_name='clv.animal.mng',
        relation='clv_animal_mng_address_confirm_rel',
        string='Animals (Management)',
        default=_default_animal_mng_ids
    )

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_animal_mng_address_confirm(self):
        self.ensure_one()

        if self.history_marker_id.id is False:
            raise exceptions.ValidationError('The "History Marker" has not been defined!')
            return self._reopen_form()

        for animal_mng in self.animal_mng_ids:

            _logger.info(u'>>>>> %s', animal_mng.name)

            if animal_mng.action_address == 'confirm':

                _logger.info(u'>>>>>>>>>> %s: %s', 'action_address', animal_mng.action_address)

                animal_mng.address_id.history_marker_id = self.history_marker_id.id

        return True

    @api.multi
    def do_populate_all_animal_mngs(self):
        self.ensure_one()

        AnimalMng = self.env['clv.animal.mng.address_confirm']
        animal_mngs = AnimalMng.search([])

        self.animal_mng_ids = animal_mngs

        return self._reopen_form()
