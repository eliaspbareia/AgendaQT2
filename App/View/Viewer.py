from PySide2.QtGui import QImage, QPainter, QPixmap
from PySide2.QtWidgets import QWidget, QStackedWidget
import os

class StackedWidget(QStackedWidget):
    def __init__(self):
        QStackedWidget.__init__(self)
        self.image = QImage()

    def set_image(self, filename):
        self.image.load(filename)

    def paintEnvent(self, event):
        painter = QPainter(self)
        imgdir = os.path.join(os.path.dirname(__file__), 'images')
        filename = imgdir + '\\PPPOS.jpg'
        if self.image:
            painter.drawPixmap(self.rect(), QPixmap(filename))
            QStackedWidget.paintEvent(self, event)