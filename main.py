import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUi


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("mainui.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
