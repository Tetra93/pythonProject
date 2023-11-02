import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal


class SubWindow(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, main_ui):
        super(SubWindow, self).__init__()
        loadUi("sub.ui", self)

        self.close_button.clicked.connect(self.close)
        self.main_ui = main_ui

        self.spinBox_1_value = 0
        self.spinBox_2_value = 0

        self.spinBox.valueChanged.connect(self.spinBox_on_changed)
        self.spinBox_2.valueChanged.connect(self.spinBox_2_on_changed)
        self.total_button.clicked.connect(self.total)

    def spinBox_on_changed(self, value):
        self.spinBox_1_value = value

    def spinBox_2_on_changed(self, value):
        self.spinBox_2_value = value

    def total(self):
        total = self.spinBox_1_value + self.spinBox_2_value
        self.label.setText(str(total))

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
