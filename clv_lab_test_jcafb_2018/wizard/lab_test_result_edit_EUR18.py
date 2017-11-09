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
    # EUR18
    #

    def _default_is_EUR18(self):
        active_id = self.env['clv.lab_test.result'].browse(self._context.get('active_id'))
        if active_id.lab_test_type_id.code == 'EUR18':
            is_EUR18 = True
        else:
            is_EUR18 = False
        return is_EUR18
    is_EUR18 = fields.Boolean('Is EUR18', readonly=True, default=_default_is_EUR18)

    def _default_EUR18_data_entrada_material(self):
        return self._get_default('EUR18', 'EUR18-01-01')
    EUR18_data_entrada_material = fields.Date(
        'Data de Entrada do Material', readonly=False, default=_default_EUR18_data_entrada_material
    )

    def _write_EUR18_data_entrada_material(self):
        self._set_result('EUR18', 'EUR18-01-01', self.EUR18_data_entrada_material)

    def _default_EUR18_liberacao_resultado(self):
        return self._get_default('EUR18', 'EUR18-01-02')
    EUR18_liberacao_resultado = fields.Date(
        'Liberação do Resultado', readonly=False, default=_default_EUR18_liberacao_resultado
    )

    def _write_EUR18_liberacao_resultado(self):
        self._set_result('EUR18', 'EUR18-01-02', self.EUR18_liberacao_resultado)

    def _default_EUR18_examinador(self):
        employee_model = self.env['hr.employee']
        code = self._get_default('EUR18', 'EUR18-01-03')
        if code is not False:
            code = code[code.find('[') + 1:code.find(']')]
            employee_search = employee_model.search([
                ('code', '=', code),
            ])
            return employee_search
        else:
            return False
    EUR18_examinador = fields.Many2one(
        'hr.employee',
        string='Examinador',
        readonly=False,
        default=_default_EUR18_examinador
    )

    def _write_EUR18_examinador(self):
        self._set_result(
            'EUR18', 'EUR18-01-03',
            self.EUR18_examinador.name + ' [' + self.EUR18_examinador.code + ']'
        )

    def _default_EUR18_volume(self):
        return self._get_default('EUR18', 'EUR18-02-01')
    EUR18_volume = fields.Char(
        'Volume', readonly=False, default=_default_EUR18_volume
    )

    def _write_EUR18_volume(self):
        self._set_result('EUR18', 'EUR18-02-01', self.EUR18_volume)

    def _default_EUR18_densidade(self):
        return self._get_default('EUR18', 'EUR18-02-02')
    EUR18_densidade = fields.Char(
        'Densidade', readonly=False, default=_default_EUR18_densidade
    )

    def _write_EUR18_densidade(self):
        self._set_result('EUR18', 'EUR18-02-02', self.EUR18_densidade)

    def _default_EUR18_aspecto(self):
        return self._get_default('EUR18', 'EUR18-02-03')
    EUR18_aspecto = fields.Selection([
        ('Límpido', 'Límpido'),
        ('Ligeiramente Turvo', 'Ligeiramente Turvo'),
        ('Turvo', 'Turvo'),
    ], 'Aspecto', readonly=False, default=_default_EUR18_aspecto)

    def _write_EUR18_aspecto(self):
        self._set_result('EUR18', 'EUR18-02-03', self.EUR18_aspecto)

    def _default_EUR18_cor(self):
        return self._get_default('EUR18', 'EUR18-02-04')
    EUR18_cor = fields.Selection([
        ('Amarelo Palha', 'Amarelo Palha'),
        ('Amarelo Claro', 'Amarelo Claro'),
        ('Amarelo Citrino', 'Amarelo Citrino'),
        ('Amarelo Ouro', 'Amarelo Ouro'),
        ('Eritrocrômica', 'Eritrocrômica'),
        ('Âmbar', 'Âmbar'),
    ], 'Cor', readonly=False, default=_default_EUR18_cor)

    def _write_EUR18_cor(self):
        self._set_result('EUR18', 'EUR18-02-04', self.EUR18_cor)

    def _default_EUR18_odor(self):
        return self._get_default('EUR18', 'EUR18-02-05')
    EUR18_odor = fields.Selection([
        ('Sui Generis', 'Sui Generis'),
        ('Pútrido', 'Pútrido'),
    ], 'Cor', readonly=False, default=_default_EUR18_odor)

    def _write_EUR18_odor(self):
        self._set_result('EUR18', 'EUR18-02-05', self.EUR18_odor)

    def _default_EUR18_ph(self):
        return self._get_default('EUR18', 'EUR18-03-01')
    EUR18_ph = fields.Char(
        'pH', readonly=False, default=_default_EUR18_ph
    )

    def _write_EUR18_ph(self):
        self._set_result('EUR18', 'EUR18-03-01', self.EUR18_ph)

    def _default_EUR18_proteinas(self):
        return self._get_default('EUR18', 'EUR18-03-02')
    EUR18_proteinas = fields.Selection([
        ('Negativo', 'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Proteina', readonly=False, default=_default_EUR18_proteinas)

    def _write_EUR18_proteinas(self):
        self._set_result('EUR18', 'EUR18-03-02', self.EUR18_proteinas)

    def _default_EUR18_glicose(self):
        return self._get_default('EUR18', 'EUR18-03-03')
    EUR18_glicose = fields.Selection([
        ('Negativo', 'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Glicose', readonly=False, default=_default_EUR18_glicose)

    def _write_EUR18_glicose(self):
        self._set_result('EUR18', 'EUR18-03-03', self.EUR18_glicose)

    def _default_EUR18_cetona(self):
        return self._get_default('EUR18', 'EUR18-03-04')
    EUR18_cetona = fields.Selection([
        ('Negativo', 'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Cetona', readonly=False, default=_default_EUR18_cetona)

    def _write_EUR18_cetona(self):
        self._set_result('EUR18', 'EUR18-03-04', self.EUR18_cetona)

    def _default_EUR18_pigmentos_biliares(self):
        return self._get_default('EUR18', 'EUR18-03-05')
    EUR18_pigmentos_biliares = fields.Selection([
        ('Negativo', 'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Pigmentos biliares', readonly=False, default=_default_EUR18_pigmentos_biliares)

    def _write_EUR18_pigmentos_biliares(self):
        self._set_result('EUR18', 'EUR18-03-05', self.EUR18_pigmentos_biliares)

    def _default_EUR18_sangue(self):
        return self._get_default('EUR18', 'EUR18-03-06')
    EUR18_sangue = fields.Selection([
        ('Negativo', 'Negativo'),
        (u'Traços', u'Traços'),
        ('(+)', '(+)'),
        ('(++)', '(++)'),
        ('(+++)', '(+++)'),
        ('(++++)', '(++++)'),
    ], 'Sangue', readonly=False, default=_default_EUR18_sangue)

    def _write_EUR18_sangue(self):
        self._set_result('EUR18', 'EUR18-03-06', self.EUR18_sangue)

    def _default_EUR18_urobilinogenio(self):
        return self._get_default('EUR18', 'EUR18-03-07')
    EUR18_urobilinogenio = fields.Selection([
        ('Normal', 'Normal'),
        (u'Positivo até Diluição de 1/80', u'Positivo até Diluição de 1/80'),
    ], 'Urobilinogênio', readonly=False, default=_default_EUR18_urobilinogenio)

    def _write_EUR18_urobilinogenio(self):
        self._set_result('EUR18', 'EUR18-03-07', self.EUR18_urobilinogenio)

    def _default_EUR18_nitrito(self):
        return self._get_default('EUR18', 'EUR18-03-08')
    EUR18_nitrito = fields.Selection([
        ('Negativo', 'Negativo'),
        ('Positivo', 'Positivo'),
    ], 'Nitrito', readonly=False, default=_default_EUR18_nitrito)

    def _write_EUR18_nitrito(self):
        self._set_result('EUR18', 'EUR18-03-08', self.EUR18_nitrito)

    def _default_EUR18_celulas_epiteliais(self):
        return self._get_default('EUR18', 'EUR18-04-01')
    EUR18_celulas_epiteliais = fields.Selection([
        ('Ausente', 'Ausente'),
        ('Raras', 'Raras'),
        ('Frequentes', 'Frequentes'),
        ('Numerosas', 'Numerosas'),
    ], 'Células Epiteliais', readonly=False, default=_default_EUR18_celulas_epiteliais)

    def _write_EUR18_celulas_epiteliais(self):
        self._set_result('EUR18', 'EUR18-04-01', self.EUR18_celulas_epiteliais)

    def _default_EUR18_muco(self):
        return self._get_default('EUR18', 'EUR18-04-02')
    EUR18_muco = fields.Selection([
        ('Ausente', 'Ausente'),
        ('Raros Filamentos', 'Raros Filamentos'),
        ('Frequentes Filamentos', 'Frequentes Filamentos'),
        ('Numerosos Filamentos', 'Numerosos Filamentos'),
    ], 'Muco', readonly=False, default=_default_EUR18_muco)

    def _write_EUR18_muco(self):
        self._set_result('EUR18', 'EUR18-04-02', self.EUR18_muco)

    def _default_EUR18_cristais(self):
        return self._get_default('EUR18', 'EUR18-04-03')
    EUR18_cristais = fields.Selection([
        (u'Ausentes', u'Ausentes'),
        (u'Raros de Oxalato de Cálcio', u'Raros de Oxalato de Cálcio'),
        (u'Frequentes de Oxalato de Cálcio', u'Frequentes de Oxalato de Cálcio'),
        (u'Numerosos de Urato Amorfo', u'Numerosos de Urato Amorfo'),
        (u'Raros de Fosfato Amorfo', u'Raros de Fosfato Amorfo'),
        (u'Raros de Fosfato Triplo, Amoníaco', u'Raros de Fosfato Triplo, Amoníaco'),
        (u'Numerosos de Fosfato Amorfo', u'Numerosos de Fosfato Amorfo'),
        (u'Frequentes de Fosfato Amorfo', u'Frequentes de Fosfato Amorfo'),
        (u'Raros de Ácido Úrico', u'Raros de Ácido Úrico'),
    ], 'Cristais', readonly=False, default=_default_EUR18_cristais)

    def _write_EUR18_cristais(self):
        self._set_result('EUR18', 'EUR18-04-03', self.EUR18_cristais)

    def _default_EUR18_leucocitos(self):
        return self._get_default('EUR18', 'EUR18-04-04')
    EUR18_leucocitos = fields.Char(
        'Leucócitos', readonly=False, default=_default_EUR18_leucocitos
    )

    def _write_EUR18_leucocitos(self):
        self._set_result('EUR18', 'EUR18-04-04', self.EUR18_leucocitos)

    def _default_EUR18_hemacias(self):
        return self._get_default('EUR18', 'EUR18-04-05')
    EUR18_hemacias = fields.Char(
        'Hemácias', readonly=False, default=_default_EUR18_hemacias
    )

    def _write_EUR18_hemacias(self):
        self._set_result('EUR18', 'EUR18-04-05', self.EUR18_hemacias)

    def _default_EUR18_cilindros(self):
        return self._get_default('EUR18', 'EUR18-04-06')
    EUR18_cilindros = fields.Selection([
        ('Ausente', 'Ausente'),
        ('Presentes', 'Presentes'),
    ], 'Cilindros', readonly=False, default=_default_EUR18_cilindros)

    def _write_EUR18_cilindros(self):
        self._set_result('EUR18', 'EUR18-04-06', self.EUR18_cilindros)

    def _default_EUR18_cilindros_hialinos(self):
        return self._get_default('EUR18', 'EUR18-04-07')
    EUR18_cilindros_hialinos = fields.Char(
        'Cilindros Hialinos', readonly=False, default=_default_EUR18_cilindros_hialinos
    )

    def _write_EUR18_cilindros_hialinos(self):
        self._set_result('EUR18', 'EUR18-04-07', self.EUR18_cilindros_hialinos)

    def _default_EUR18_cilindros_granulosos(self):
        return self._get_default('EUR18', 'EUR18-04-08')
    EUR18_cilindros_granulosos = fields.Char(
        'Cilindros Granulosos', readonly=False, default=_default_EUR18_cilindros_granulosos
    )

    def _write_EUR18_cilindros_granulosos(self):
        self._set_result('EUR18', 'EUR18-04-08', self.EUR18_cilindros_granulosos)

    def _default_EUR18_cilindros_leucocitarios(self):
        return self._get_default('EUR18', 'EUR18-04-09')
    EUR18_cilindros_leucocitarios = fields.Char(
        'Cilindros Leucocitários', readonly=False, default=_default_EUR18_cilindros_leucocitarios
    )

    def _write_EUR18_cilindros_leucocitarios(self):
        self._set_result('EUR18', 'EUR18-04-09', self.EUR18_cilindros_leucocitarios)

    def _default_EUR18_cilindros_hematicos(self):
        return self._get_default('EUR18', 'EUR18-04-10')
    EUR18_cilindros_hematicos = fields.Char(
        'Cilindros Hemáticos', readonly=False, default=_default_EUR18_cilindros_hematicos
    )

    def _write_EUR18_cilindros_hematicos(self):
        self._set_result('EUR18', 'EUR18-04-10', self.EUR18_cilindros_hematicos)

    def _default_EUR18_cilindros_cereos(self):
        return self._get_default('EUR18', 'EUR18-04-11')
    EUR18_cilindros_cereos = fields.Char(
        'Cilindros Céreos', readonly=False, default=_default_EUR18_cilindros_cereos
    )

    def _write_EUR18_cilindros_cereos(self):
        self._set_result('EUR18', 'EUR18-04-11', self.EUR18_cilindros_cereos)

    def _default_EUR18_outros_tipos_de_cilindros(self):
        return self._get_default('EUR18', 'EUR18-04-12')
    EUR18_outros_tipos_de_cilindros = fields.Char(
        'Outros tipos de Cilindros', readonly=False, default=_default_EUR18_outros_tipos_de_cilindros
    )

    def _write_EUR18_outros_tipos_de_cilindros(self):
        self._set_result('EUR18', 'EUR18-04-12', self.EUR18_outros_tipos_de_cilindros)

    def _default_EUR18_obs(self):
        return self._get_default('EUR18', 'EUR18-05-01')
    EUR18_obs = fields.Char(
        'Observações', readonly=False, default=_default_EUR18_obs
    )

    def _write_EUR18_obs(self):
        self._set_result('EUR18', 'EUR18-05-01', self.EUR18_obs)

    def _do_result_updt_EUR18(self):

        self._write_EUR18_data_entrada_material()
        self._write_EUR18_liberacao_resultado()
        self._write_EUR18_examinador()
        self._write_EUR18_volume()
        self._write_EUR18_densidade()
        self._write_EUR18_aspecto()
        self._write_EUR18_cor()
        self._write_EUR18_odor()
        self._write_EUR18_ph()
        self._write_EUR18_proteinas()
        self._write_EUR18_glicose()
        self._write_EUR18_cetona()
        self._write_EUR18_pigmentos_biliares()
        self._write_EUR18_sangue()
        self._write_EUR18_urobilinogenio()
        self._write_EUR18_nitrito()
        self._write_EUR18_celulas_epiteliais()
        self._write_EUR18_muco()
        self._write_EUR18_cristais()
        self._write_EUR18_leucocitos()
        self._write_EUR18_hemacias()
        self._write_EUR18_cilindros()
        self._write_EUR18_cilindros_hialinos()
        self._write_EUR18_cilindros_granulosos()
        self._write_EUR18_cilindros_leucocitarios()
        self._write_EUR18_cilindros_hematicos()
        self._write_EUR18_cilindros_cereos()
        self._write_EUR18_outros_tipos_de_cilindros()
        self._write_EUR18_obs()

        return True
