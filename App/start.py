import sys
from PySide2.QtWidgets import (QApplication)
from App.Include.Widget import Widget
from App.View.Application import Application

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Application()
    widget.start()

    # widget = Widget()
    # window = Application(widget)
    # window.start()

    sys.exit(app.exec_())