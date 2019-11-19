from PySide2.QtWidgets import (QWidget, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, QDialogButtonBox)
from PySide2.QtCore import Qt

from App.Include.List import Listagem
from App.Include.Form import Form
from App.Model.Dataset import Dataset as dataset
from App.Model.Person import Person as model
from App.Include.Util import Util


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.campos = {
            "nome": {
                "titulo": "Nome",
                "tipo": "text",
                "required": "True"
            },
            # "cpf":{
            #     "titulo": "CPF",
            #     "tipo": "text",
            #     "required": "True"
            # },
            "email": {
                "titulo": "Email",
                "tipo": "email",
                "required": "True"
            },
            "celular": {
                "titulo": "Celular",
                "tipo": "phone",
                "required": "True"
            },
            "dtanascimento": {
                "titulo": "Nascimento",
                "tipo": "date",
                "required": "True"
            }
        }
        self.selection = None
        self.listagem = Listagem()
        """
        Observação: se for passado campos como argumento, a proxima class os receberá com truple
                    caso seja passado como kwords, a proxima class os receberá como dict
        """
        self.formulario = Form(**self.campos)
        self.initGui()
        self.contatos = self.preencherlistagem()
        self.listagem.bind_doble_click(self.showfields)
        self.rowid = None

    def initGui(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.listagem)

        vbox = QVBoxLayout()
        vbox.addWidget(self.formulario)

        vbox.addStretch(1)

        # Botoes
        self.newBtn = QPushButton(self.tr("&Limpa"))
        self.newBtn.setDefault(True)
        self.delBtn = QPushButton(self.tr("&Delete"))
        self.delBtn.clicked.connect(self.delete)
        self.newBtn.clicked.connect(self.new)
        self.saveBtn = QPushButton(self.tr("&Save"))
        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn = QPushButton(self.tr("&Fechar"))
        self.cancelBtn.clicked.connect(self.cancel)
        self.cancelBtn.setCheckable(True)
        self.cancelBtn.setAutoDefault(False)

        self.buttonBox = QDialogButtonBox(Qt.Horizontal)
        self.buttonBox.addButton(self.newBtn, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.delBtn, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.saveBtn, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.cancelBtn, QDialogButtonBox.AcceptRole)
        vbox.addWidget(self.buttonBox)

        hbox.addLayout(vbox)
        self.setLayout(hbox)

    def preencherlistagem(self):
        records = dataset.select(model).group_by(model.id)
        rows = []
        for row in records:
            self.listagem.insert(row.nomeperson)
            rows.append(row)
        return rows

    def showfields(self, index):
        self.selection = index.row()
        row = self.contatos[index.row()]
        records = dataset.selectbyid(model, row)
        l = list()
        for r in records:
            self.rowid = r.id
            l.append(r.id)
            l.append(r.nomeperson)
            l.append(r.emailperson)
            l.append(r.telefoneperson)
            l.append(r.dtanascimentoperson)
        self.formulario.lerdetalhes(l)
        self.newBtn.setEnabled(True)
        # Cor normal do edit
        for e in self.formulario.entries:
            e.setStyleSheet("border: 1px solid gray")

    def new(self):
        self.formulario.limpaValores()
        self.newBtn.setEnabled(False)
        self.rowid = None

    def delete(self):
        if self.selection is None:
            self.messagem('Aviso', 'Selecione um registro primeiro')
            return
        try:
            _id = self.contatos[self.selection]
            record = dataset.delete(model, _id)
        except ValueError as e:
            self.messagem('Erro', e)
        else:
            if record == 1:
                self.messagem('Sucesso', 'Registro deletado com sucesso')
                self.formulario.limpaValores()
                self.listagem.delete(self.selection)
                del self.contatos[self.selection]
                self.listagem.limpar()
                self.preencherlistagem()
            else:
                self.messagem('Erro', 'Ocorreu algum erro, tente novamente.')

    def save(self):
        self.newBtn.setEnabled(True)
        valores = self.formulario.pegaValores()
        v = {}
        if 'id' in valores:
            v['id'] = valores['id']
        v['nomeperson'] = valores['nome']
        v['emailperson'] = valores['email']
        v['dtanascimentoperson'] = Util.format_data_entry_widget(valores['dtanascimento'])
        v['telefoneperson'] = valores['celular']

        if self.rowid:
            # Atualização
            try:
                dataset.update(model, v)
            except ValueError as erro:
                self.messagem('Aviso', erro)
            else:
                self.listagem.limpar()
                self.preencherlistagem()

        else:
            # Inserção
            for e in self.formulario.entries:
                if e.objectName() == "nome":
                    if not e.text():
                        QMessageBox.warning(self, self.tr("Verificação de Nome"), self.tr("O Campo não pode está fazio"), QMessageBox.Ok)
                        e.setFocus()
                        return
            try:
                retorno = dataset.insert(model, v)
            except ValueError as erro:
                self.messagem('Aviso', erro)
            else:
                self.listagem.limpar()
                self.preencherlistagem()
                self.contatos.append(retorno)

    def cancel(self):
        self.close()

    def messagem(self, tipo, msg):
        msbBox = QMessageBox()
        msbBox.setWindowTitle(tipo)
        msbBox.setText(msg)
        msbBox.exec_()


