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
import xlwt

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestOffReport(models.Model):
    _name = "clv.lab_test.off.report"
    _inherit = 'clv.lab_test.off.report'

    def lab_test_off_report_export_templates_dir_path(self):
        return '/opt/openerp/clvsol_clvhealth_jcafb/lab_test_files/reports/templates'

    def lab_test_off_report_export_xls_dir_path(self):
        return '/opt/openerp/clvsol_clvhealth_jcafb/lab_test_files/reports/xls'

    def lab_test_off_report_export_xls_file_name(self):
        return 'Laudo_<type>_<request_code>.xls'

    def lab_test_off_report_export_xls(self, dir_path, file_name):

        lab_test_type = self.lab_test_type_id.code
        lab_test_request_code = self.lab_test_request_id.code

        FileSystemDirectory = self.env['clv.file_system.directory']
        file_system_directory = FileSystemDirectory.search([
            ('directory', '=', dir_path),
        ])

        file_name = file_name.replace('<type>', lab_test_type).replace('<request_code>', lab_test_request_code)

        file_path = dir_path + '/' + file_name
        _logger.info(u'%s %s', '>>>>>>>>>>', file_path)

        book = xlwt.Workbook()

        sheet = book.add_sheet(file_name)
        row_nr = 0

        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Person:')
        row.write(3, self.person_id.name)
        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Lab Test Type:')
        row.write(3, lab_test_type)
        row_nr += 1
        row = sheet.row(row_nr)
        row.write(0, 'Request Code:')
        row.write(3, lab_test_request_code)
        row_nr += 1

        book.save(file_path)

        self.directory_id = file_system_directory.id
        self.file_name = file_name
        self.stored_file_name = file_name

        return True
