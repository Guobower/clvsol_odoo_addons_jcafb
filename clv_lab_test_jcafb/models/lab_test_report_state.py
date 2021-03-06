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

from openerp import api, fields, models
from openerp.exceptions import UserError


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.report'

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('approved', 'Approved'),
         ('discarded', 'Discarded')
         ], string='State', default='new', readonly=True, required=True
    )

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        # allowed = [
        #     ('discarded', 'new'),
        #     ('new', 'available'),
        # ]
        # return (old_state, new_state) in allowed
        return True

    @api.multi
    def change_state(self, new_state):
        for lab_test_report in self:
            if lab_test_report.is_allowed_transition(lab_test_report.state, new_state):
                lab_test_report.state = new_state
            else:
                raise UserError('Status transition (' + lab_test_report.state + ', ' + new_state + ') is not allowed!')

    @api.multi
    def action_new(self):
        for lab_test_report in self:
            lab_test_report.change_state('new')

    @api.multi
    def action_available(self):
        for lab_test_report in self:
            lab_test_report.change_state('available')

    @api.multi
    def action_approve(self):
        for lab_test_report in self:
            lab_test_report.change_state('approved')

    @api.multi
    def action_discard(self):
        for lab_test_report in self:
            lab_test_report.change_state('discarded')
