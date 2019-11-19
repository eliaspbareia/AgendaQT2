from PySide2.QtWidgets import (QDateEdit, QLineEdit, QVBoxLayout, QFrame, QFormLayout)
from PySide2.QtCore import *
from PySide2.QtGui import QRegExpValidator

"""
Principais componentes:
QLineEdit 
QTextEdit
QDateEdit
"""
"""
       O argumento campos foi declarado como kwords por ser um dict
       Acesso ao dicionario campos se faz da seguinte forma:
       campos['nome']['titulo']
       
       Falta melhorar as validações evitando o nome dos campos
"""
class Form(QFrame):

    def __init__(self, **campos):
        QFrame.__init__(self)
        self.validator = None
        self.fields = campos
        self.formlayout = QFormLayout()
        self.entries = list(map(self.addField, campos))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.formlayout)
        self.setLayout(self.mainLayout)
        self.rowid = 0

    def addField(self, field):
        if self.fields[field]['tipo'] == 'text':
            self.entry = QLineEdit()
            self.entry.setObjectName(self.tr(field))
            self.formlayout.addRow(self.fields[field]['titulo'], self.entry)
        if self.fields[field]['tipo'] == 'email':
            self.entry = QLineEdit()
            self.entry.setObjectName(self.tr(field))
            regexp = QRegExp("[^@]+@[^@]+\.[^@]+")
            self.entry.setValidator(QRegExpValidator(regexp))
            self.entry.textChanged.connect(self.adjustTextColor)
            self.formlayout.addRow(self.fields[field]['titulo'], self.entry)
        if self.fields[field]['tipo'] == 'phone':
            self.entry = QLineEdit()
            self.entry.setObjectName(self.tr(field))
            self.entry.setPlaceholderText("(63)3939-3939")
            regexp = QRegExp("(\(\d{2}\))(\d{4,5}\-\d{4})")
            self.entry.setValidator(QRegExpValidator(regexp))
            self.entry.textChanged.connect(self.phoneAdjustTextColor)
            self.formlayout.addRow(self.fields[field]['titulo'], self.entry)
        if self.fields[field]['tipo'] == 'date':
            self.entry = QDateEdit()
            self.entry.setDate(QDate.currentDate())
            self.entry.setObjectName(self.tr(field))
            self.formlayout.addRow(self.fields[field]['titulo'], self.entry)
        """ Acrescentar tipo cpf"""
        return self.entry

    def lerdetalhes(self, records):
        self.rowid = records[0]
        records.remove(records[0])

        for entry, value in zip(self.entries, records):
            if type(entry) == QDateEdit:
                entry.setDate(value)
            elif type(entry) == QLineEdit:
                entry.setText(value)


    def pegaValores(self):
        values = list()
        fields = list()
        if self.rowid:
            fields.append('id')
            values.append(self.rowid)
        for f in self.fields:
            fields.append(f)
        for entry in self.entries:
            values.append(entry.text())
        try:
            return dict(zip(fields, values))
        except ValueError as e:
            print(e)

    def limpaValores(self):
        if self.rowid:
            self.rowid = 0
        for entry in self.entries:
            if type(entry) == QDateEdit:
                pass
            else:
                entry.clear()

    def adjustTextColor(self):
        for entry in self.entries:
            if entry.objectName() == 'email':
                if not entry.hasAcceptableInput():
                    entry.setStyleSheet("color: red")

                else:
                    entry.setStyleSheet("color: black")


    def phoneAdjustTextColor(self):
        for entry in self.entries:
            if entry.objectName() == 'celular':
                if not entry.hasAcceptableInput():
                    entry.setStyleSheet("color: red")

                else:
                    entry.setStyleSheet("color: black")