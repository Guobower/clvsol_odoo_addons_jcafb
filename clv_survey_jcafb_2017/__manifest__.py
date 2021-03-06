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

{
    'name': 'JCAFB Surveys (2017)',
    'summary': 'This module will install all the JCAFB surveys (2017).',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_survey_jcafb',
    ],
    'data': [
        'data/survey_jcafb_QAN17.xml',
        'data/survey_jcafb_QDH17.xml',
        'data/survey_jcafb_QMD17.xml',
        'data/survey_jcafb_QSC17.xml',
        'data/survey_jcafb_QSF17.xml',
        'data/survey_jcafb_QSI17.xml',
        'data/survey_jcafb_TCP17.xml',
        'data/survey_jcafb_TCR17.xml',
        'data/survey_jcafb_TID17.xml',

        'data/document_jcafb_TCP17.xml',
        'data/document_jcafb_TCR17.xml',
        'data/document_jcafb_TID17.xml',

        'wizard/document_item_edit_TCP17_view.xml',
        'wizard/document_item_edit_TCR17_view.xml',
        'wizard/document_item_edit_TID17_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
