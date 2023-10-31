import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUi

import sub
from sub import SubWindow


class MainUI(QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("mainWindow.ui", self)
        self.pushButton.clicked.connect(self.on_click)
        self.sub_ui = None

    def on_click(self):
        self.hide()
        self.sub_ui = sub.SubWindow(self)
        self.sub_ui.show()
        self.sub_ui.closed.connect(self.show_main_ui)

    def show_main_ui(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
