from tkinter import *
from datetime import datetime, date


class Util:

    def format_fone_entry_widget(value):
        # (63)99935-5687
        value = value.replace("(", "").replace(")", "").replace("-", "")
        if len(value) == 10:
            return "({0}{1}){2}{3}{4}{5}-{6}{7}{8}{9}".format(*value)
        elif len(value) == 11:
            return "({0}{1}){2}{3}{4}{5}{6}-{7}{8}{9}{10}".format(*value)
        else:
            return {'mensagem':'O Telefone deve conter no mínimo 10 digitos\n no formato (00)00000-0000'}

    @staticmethod
    def format_fone_entry_widget2(value):
        value = value.replace("(", "").replace(")", "").replace("-", "")
        if len(value) == 10 or len(value) == 11:
            return True
        else:
            return False

    def format_data_entry_widget(value):
        try:
            valor_retorno = datetime.strptime(value, '%d/%m/%Y').date()
        except ValueError:
            return False
        else:
            return valor_retorno

    @staticmethod
    def decode_data_entry_widget(value):
        try:
            valor_retorno = value.strftime("%m/%d/%Y")
        except ValueError:
            return False
        else:
            return valor_retorno

    @staticmethod
    def format_email_entry_widget(value):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not email_regex.match(value):
            return False
        return True

    @staticmethod
    def valida(values):
        # {'nome': '', 'email': '', 'celular': '()-', 'dtanascimento': '18/11/2019'}
        vz = []
        for k, v in values.items():
            vz.append(Util.verifica_vazio(v))
        if 'email' in values:
            email = Util.format_email_entry_widget(values['email'])
        if 'celular' in values:
            celular = Util.format_fone_entry_widget2(values['celular'])
        rt = vz[0:2]
        rt.append(email)
        rt.append(celular)
        return rt


    @staticmethod
    def verifica_vazio(texto):
        if len(texto) == 0:
            return False
        else:
            return True