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


class AnimalDocumentSetup(models.TransientModel):
    _inherit = 'clv.animal.document_setup'

    def _default_history_marker_id(self):
        HistoryMarker = self.env['clv.history_marker']
        history_marker = HistoryMarker.search([
            ('name', '=', 'JCAFB-2018'),
        ])
        history_marker_id = False
        if history_marker.id is not False:
            history_marker_id = history_marker.id
        return history_marker_id
    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict',
        default=_default_history_marker_id
    )

    def get_category_id(self, survey_title):

        DocumentCategory = self.env['clv.document.category']

        document_category = DocumentCategory.search([
            ('name', '=', 'Questionário'),
        ])
        category_id_questionario = False
        if document_category.id is not False:
            category_id_questionario = document_category.id

        document_category = DocumentCategory.search([
            ('name', '=', 'Termo de Consentimento'),
        ])
        category_id_termo = False
        if document_category.id is not False:
            category_id_termo = document_category.id

        category_id = False

        if (survey_title == '[QVG18]') or \
           (survey_title == '[QVI18]'):
            category_id = category_id_questionario

        if (survey_title == '[TCV18]'):
            category_id = category_id_termo

        return category_id
