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

from odoo import api, models

_logger = logging.getLogger(__name__)


class DocumentTypeItemSetUp(models.TransientModel):
    _inherit = 'clv.document.type.item_setup'

    @api.multi
    def _do_document_type_item_setup(self, document_type):
        self.ensure_one()

        Survey = self.env['survey.survey']
        DocumentItem = self.env['clv.document.item']

        survey = Survey.search([
            ('code', '=', document_type.code),
        ])

        _logger.info(u'%s %s', '>>>>>>>>>>', survey.code)

        document_items = DocumentItem.search([
            ('document_type_id', '=', document_type.id),
        ])
        document_items.unlink()

        items = []
        sequence = 0

        for page in survey.page_ids:

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>>', page.code)

            _title_ = page.title.encode("utf-8")

            sequence += 1
            items.append((0, 0, {'code': page.code,
                                 'name': _title_,
                                 'sequence': sequence,
                                 }))

            for question in page.question_ids:

                _logger.info(u'%s %s', '>>>>>>>>>>>>>>>>>>>>', question.code)

                _type_ = question.type
                _question_ = question.question.encode("utf-8")

                sequence += 1
                items.append((0, 0, {'code': question.code,
                                     'name': _question_,
                                     'sequence': sequence,
                                     }))

                if question.comments_allowed is True:

                    if question.comments_message is not False:
                        _comments_message_ = question.comments_message.encode("utf-8")

                    sequence += 1
                    items.append((0, 0, {'code': question.code + '_C',
                                         'name': _comments_message_,
                                         'sequence': sequence,
                                         }))

                if _type_ == 'free_text' or _type_ == 'textbox' or _type_ == 'datetime':
                    pass

                if _type_ == 'simple_choice':
                    pass

                if _type_ == 'multiple_choice':
                    pass

                if _type_ == 'matrix':

                    for label in question.labels_ids_2:

                        _value_ = label.value.encode("utf-8")

                        sequence += 1
                        items.append((0, 0, {'code': label.code,
                                             'name': _value_,
                                             'sequence': sequence,
                                             }))

        document_type.item_ids = items

        return True
