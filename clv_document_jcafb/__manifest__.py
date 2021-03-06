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
    'name': 'Document (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Document Module customizations for CLVhealth-JCAFB Solution.',
    'version': '3.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_document',
        'clv_survey',
        'clv_address_jcafb',
        'clv_person_jcafb',
        'clv_animal_jcafb',
    ],
    'data': [
        'views/document_code_view.xml',
        'views/document_reg_state_view.xml',
        'views/document_state_view.xml',
        'views/document_view.xml',
        'views/person_view.xml',
        'views/address_view.xml',
        'views/animal_view.xml',
        'data/document_seq.xml',
        'wizard/document_updt_view.xml',
        'wizard/document_item_edit_view.xml',
        'wizard/document_item_updt_from_survey_view.xml',
        'wizard/document_type_setup_view.xml',
        'views/document_menu_view.xml',
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
