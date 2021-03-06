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
# import xlwt
from datetime import datetime

from odoo import models

_logger = logging.getLogger(__name__)


class LabTestOffReport(models.Model):
    _name = "clv.lab_test.off.report"
    _inherit = 'clv.lab_test.off.report'

    def lab_test_off_report_export_xls_EDH18(self, sheet, row_nr, logo_file_path, use_template):

        ExportXLS = self.env['clv.export_xls']

        # lab_test_type = self.lab_test_type_id.code
        lab_test_off_request_code = self.lab_test_off_request_id.code
        # lab_test_result_code = self.code

        sheet.header_str = ''
        sheet.footer_str = ''

        for i in range(0, 49):
            sheet.col(i).width = 256 * 2
        sheet.show_grid = False

        # row_nr += 2

        sheet.insert_bitmap(logo_file_path, row_nr, 3)

        ExportXLS.setOutCell(sheet, 13, row_nr, u'Jornada Científica dos Acadêmicos de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 19, row_nr, u'JCAFB-2018 - FERNÃO - SP')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 17, row_nr,
                             u'Centro Acadêmico de Farmácia-Bioquímica')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 18, row_nr,
                             u'Faculdade de Ciências Farmacêuticas')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Universidade de São Paulo')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 2, row_nr, u'Nome:')
        ExportXLS.setOutCell(sheet, 6, row_nr, self.person_off_id.name)
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Cadastro:')
        ExportXLS.setOutCell(sheet, 35, row_nr, self.person_off_id.code)
        row_nr += 2

        ExportXLS.setOutCell(sheet, 2, row_nr, u'Data do Exame:')
        if self.date_approved is not False:
            date = datetime.strptime(self.date_approved, '%Y-%m-%d')
            date = datetime.strftime(date, '%d-%m-%Y')
            ExportXLS.setOutCell(sheet, 10, row_nr, date)
        else:
            ExportXLS.setOutCell(sheet, 10, row_nr, None)
        ExportXLS.setOutCell(sheet, 30, row_nr, u'Código do Exame:')
        ExportXLS.setOutCell(sheet, 38, row_nr, lab_test_off_request_code)
        row_nr += 3

        ExportXLS.setOutCell(sheet, 4, row_nr, u'CAMPANHA PARA DETECÇÃO DE DIABETES - HIPERTENSÃO - COLESTEROL')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 20, row_nr, u'GLICEMIA')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 25, row_nr, u'Valores de referência (1)')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Jejum (mínimo de 8 hs):')
        row_nr += 1

        result = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-04-01'),
        ]).result
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Glicose:')
        if result is not False:
            ExportXLS.setOutCell(sheet, 7, row_nr, result)
        ExportXLS.setOutCell(sheet, 10, row_nr, u'mg/dL')
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Normal: <=99 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Risco aumentado para diabetes (pré-diabetes): 100 a 125 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Diabetes: > 126 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Pós-prandial ou aleatória: <140 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Material: Sangue total, colhido por punção digital.')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 2, row_nr,
                             u'Método utilizado: Leitura de tiras reagentes pelo sistema Accu-Chek Performa (Roche)')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 18, row_nr, u'COLESTEROLEMIA')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 25, row_nr, u'Valores de referência (1)')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Adulto (>20 anos):')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'2 a 19 anos:')
        row_nr += 1

        result = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-04-05'),
        ]).result
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Colesterol total:')
        if result is not False:
            ExportXLS.setOutCell(sheet, 10, row_nr, result)
        ExportXLS.setOutCell(sheet, 13, row_nr, u'mg/dL')
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Desejável : < 200 mg/dL')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'Desejável : < 150 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Limítrofe: 200 – 239 mg/dL')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'Limítrofe: 150 – 169 mg/dL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Elevado: > 240 mg/dL')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'Elevado: > 170 mg/dLL')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Material: Sangue total, colhido por punção digital.')
        row_nr += 1
        ExportXLS.setOutCell(
            sheet, 2, row_nr,
            u'Método utilizado: Colesterol total: leitura de tiras reagentes pelo sistema Accutrend Cholesterol (Roche)'
        )
        row_nr += 3

        ExportXLS.setOutCell(sheet, 15, row_nr, u'MEDIDA DE PRESSÃO ARTERIAL (mmHg)')
        row_nr += 2

        ExportXLS.setOutCell(sheet, 25, row_nr, u'Valores de referência (1)')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 10, row_nr, u'PAS')
        ExportXLS.setOutCell(sheet, 13, row_nr, u'PAD')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'PAS')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'PAD')
        row_nr += 1

        result_pas = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-03-06'),
        ]).result
        result_pad = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-03-07'),
        ]).result
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Pressão Arterial:')
        if result_pas is not False:
            ExportXLS.setOutCell(sheet, 10, row_nr, result_pas)
        ExportXLS.setOutCell(sheet, 12, row_nr, 'X')
        if result_pad is not False:
            ExportXLS.setOutCell(sheet, 13, row_nr, result_pad)
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Ótimo:')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'<120')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'<80')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Normal:')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'120-129')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'80-84')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Limítrofe:')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'130-139')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'85-89')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 20, row_nr, u'Hipertensão:')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'>140')
        ExportXLS.setOutCell(sheet, 35, row_nr, u'>90')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Método utilizado: Esfigmomanometria.')
        row_nr += 3

        ExportXLS.setOutCell(sheet, 2, row_nr, u'Informações complementares')
        row_nr += 2

        result_peso = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-02-01'),
        ]).result
        result_altura = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-02-03'),
        ]).result
        result_circunf = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-02-09'),
        ]).result
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Peso:')
        if result_peso is not False:
            ExportXLS.setOutCell(sheet, 5, row_nr, result_peso)
        ExportXLS.setOutCell(sheet, 7, row_nr, 'kg')
        ExportXLS.setOutCell(sheet, 15, row_nr, 'Altura:')
        if result_altura is not False:
            ExportXLS.setOutCell(sheet, 19, row_nr, result_altura)
        ExportXLS.setOutCell(sheet, 21, row_nr, u'cm')
        ExportXLS.setOutCell(sheet, 27, row_nr, u'Circunferência abdominal:')
        if result_circunf is not False:
            ExportXLS.setOutCell(sheet, 39, row_nr, result_circunf)
        ExportXLS.setOutCell(sheet, 41, row_nr, u'cm')
        row_nr += 2

        result = self.criterion_ids.search([
            ('lab_test_off_report_id', '=', self.id),
            ('code', '=', 'EDH18-05-01'),
        ]).result
        ExportXLS.setOutCell(sheet, 2, row_nr, u'Observações:')
        if result is not False:
            ExportXLS.setOutCell(sheet, 9, row_nr, result)
        row_nr += 3

        ExportXLS.setOutCell(sheet, 2, row_nr, u'Nota: (1): Glicemia:Critérios Diagnósticos segundo Associação Americana de Diabetes (2014); (2) Colesterol total: V Diretrizes Brasileiras de Dislipidemias e Prevenção da Aterosclerose-2013); (3): VI Diretrizes Brasileiras de Hipertensão Arterial - 2010.')

        row_nr += 4

        ExportXLS.setOutCell(sheet, 17, row_nr, u'Farmacêutico(a) Responsável:')
        row_nr += 1
        ExportXLS.setOutCell(sheet, 33, row_nr, self.employee_id.name)
        row_nr += 1
        ExportXLS.setOutCell(sheet, 36, row_nr, self.employee_id.professional_id)

        return True
