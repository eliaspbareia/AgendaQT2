import sys
from PySide2.QtWidgets import (QApplication)
from App.View.Application import Application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Window dimensions
    #app.setStyleSheet("QMainWindow {background-color: yellow}")
    widget = Application()
    widget.start()
    sys.exit(app.exec_())