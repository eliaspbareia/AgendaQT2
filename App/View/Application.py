import sys
from PySide2.QtCore import Slot, Qt, QSize
from PySide2.QtWidgets import (QMainWindow, QAction)
from PySide2.QtGui import QPixmap, QPalette
from App.Include.Widget import Widget

class Application(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Arquivo")
        self.agenda_menu = self.menu.addMenu("Agenda")
        # insere widget
        #self.setCentralWidget(widget)

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        open_action = QAction("Agenda", self)
        open_action.triggered.connect(self.open_agenda)

        self.file_menu.addAction(exit_action)
        self.agenda_menu.addAction(open_action)
        # Exibe uma imagem de fundo
        # imgdir = os.path.join(os.path.dirname(__file__), 'images')
        # filename = imgdir+'\\6HRZZVVT.jpg'
        # pix = QPixmap(filename)
        # pix.scaled(self.size(), Qt.IgnoreAspectRatio)
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, pix)
        # self.setPalette(palette)

        h = self.geometry().height()
        w = self.geometry().width()
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)

        # Status Bar
        self.status = self.statusBar()
        # self.status.setStyleSheet("background-color: gray")
        self.status.showMessage("Agenda 1.0.0", 10000)


    @Slot()
    def exit_app(self, checked):
        sys.exit()

    @Slot()
    def open_agenda(self):
        widget = Widget()
        self.setCentralWidget(widget)

    def start(self):
        self.setWindowTitle("Agenda")
        self.show()