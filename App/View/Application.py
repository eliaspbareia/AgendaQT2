import sys
import os
from PySide2.QtCore import Slot, Qt
from PySide2.QtWidgets import (QMainWindow, QAction)
from PySide2.QtGui import QPixmap, QPalette


class Application(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Arquivo")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)

        imgdir = os.path.join(os.path.dirname(__file__), 'images')
        filename = imgdir+'\\PPPOS.jpg'
        pix = QPixmap(filename)
        pix.scaled(self.size(), Qt.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.Background, pix)
        self.setPalette(palette)

        # Status Bar
        self.status = self.statusBar()
        self.status.setStyleSheet("background-color: gray")
        self.status.showMessage("Agenda 1.0.0", 10000)


    @Slot()
    def exit_app(self, checked):
        sys.exit()

    def start(self):
        self.setWindowTitle("Agenda")
        self.showMaximized()
