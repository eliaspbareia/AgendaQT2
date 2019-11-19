from PySide2.QtWidgets import (QFrame, QAbstractItemView, QFormLayout, QVBoxLayout, QLineEdit)
from PySide2.QtWidgets import QListWidget
from PySide2.QtGui import QIcon, QPixmap
from App.Model.Dataset import Dataset as dataset
from App.Model.Person import Person as model
import os


class Listagem(QFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.listView = QListWidget(self)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.listView.setMinimumHeight(385)
        # imgdir = os.path.join(os.path.dirname(__file__), 'img')
        # searchicon = QIcon()
        # searchicon.addPixmap(QPixmap(imgdir + "\search.ico"), QIcon.Normal, QIcon.Off)
        #
        # self.lineedit = QLineEdit()
        # self.lineedit.setObjectName(self.tr("nomeperson"))
        # self.lineedit.setClearButtonEnabled(True)
        # self.lineedit.addAction(searchicon, QLineEdit.LeadingPosition)
        # self.lineedit.setPlaceholderText("Localizar...")
        # self.lineedit.textChanged.connect(self.search)

        self.formlayout = QFormLayout()
       # self.formlayout.addWidget(self.lineedit)
        self.formlayout.addWidget(self.listView)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.formlayout)

        self.setLayout(self.mainLayout)

    def limpar(self):
        self.listView.clear()

    def insert(self, registro):
        self.listView.addItem(registro)

    def delete(self, index):
        self.listView.itemDelegateForRow(index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.listView.currentIndex())
        self.listView.clicked.connect(handler)
    #
    # def search(self):
    #     retorno = dataset.search(model, self.lineedit.objectName(), self.lineedit.text())
    #     for r in retorno:
    #         print(r.nomeperson)
