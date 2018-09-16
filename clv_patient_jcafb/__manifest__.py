# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Patient Module customizations for CLVhealth-JCAFB Solution.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_base_jcafb',
        'clv_patient',
        'clv_document',
        'clv_event',
        'clv_lab_test',
    ],
    'data': [
        'data/document_referenceable_model.xml',
        'data/event_referenceable_model.xml',
        'data/lab_test_referenceable_model.xml',
        'views/document_view.xml',
        'views/event_view.xml',
        'views/lab_test_view.xml',
        'views/patient_menu_view.xml',
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