import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal


class SubWindow(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, main_ui):
        super(SubWindow, self).__init__()
        loadUi("sub.ui", self)
        self.pushButton.clicked.connect(self.close)
        self.main_ui = main_ui

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
