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

_logger = logging.getLogger(__name__)


class CommunityUpdate(models.TransientModel):
    _inherit = 'clv.community.updt'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee'
    )
    employee_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Responsible Empĺoyee', default=False, readonly=False, required=False
    )

    @api.multi
    def do_community_updt(self):
        self.ensure_one()

        super(CommunityUpdate, self).do_community_updt()

        for community in self.community_ids:

            _logger.info(u'%s %s', '>>>>>', community.name)

            if self.employee_id_selection == 'set':
                community.employee_id = self.employee_id
            if self.employee_id_selection == 'remove':
                community.employee_id = False

        return True
