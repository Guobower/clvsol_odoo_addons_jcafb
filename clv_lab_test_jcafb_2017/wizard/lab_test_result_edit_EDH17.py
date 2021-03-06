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

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LabTestResultEdit(models.TransientModel):
    _inherit = 'clv.lab_test.result.edit'

    #
    # EDH17
    #

    def _default_is_EDH17(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EDH17':
            is_EDH17 = True
        else:
            is_EDH17 = False
        return is_EDH17
    is_EDH17 = fields.Boolean('Is EDH17', readonly=True, default=_default_is_EDH17)

    def _default_EDH17_tempo_jejum(self):
        return self._get_default('EDH17', 'EDH17-01-01')
    EDH17_tempo_jejum = fields.Char(
        'Tempo de Jejum', readonly=False, default=_default_EDH17_tempo_jejum
    )

    def _write_EDH17_tempo_jejum(self):
        self._set_result('EDH17', 'EDH17-01-01', self.EDH17_tempo_jejum)

    def _do_result_updt_EDH17(self):

        self._write_EDH17_tempo_jejum()

        return True
