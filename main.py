import sys
import json

from PyQt6.QtWidgets import (QMainWindow, QApplication, QPushButton,
                             QLabel, QScrollArea, QCheckBox, QWidget, QGridLayout)
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal

import sub
from sub import SubWindow


class MainUI(QMainWindow):
    with open('items.txt', 'r') as file:
        data = json.load(file)

    artifacts = data[0]

    sub_button: QPushButton
    calculate_button: QPushButton
    label1: QLabel
    label2: QLabel
    label3: QLabel
    label1_2: QLabel
    label2_2: QLabel
    label3_2: QLabel
    label1_text = 'Strength'
    label2_text = 'Defense'
    label3_text = 'Magic'
    label1_2_text = 0
    label2_2_text = 0
    label3_2_text = 0

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("mainWindow.ui", self)

        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(60, 10, 330, 180)
        self.grid = QGridLayout(self.widget)
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(60, 10, 330, 180)
        self.scroll_area.setWidget(self.widget)
        row = 0
        for key, inner_dict in self.artifacts.items():
            name_label = QLabel(key)
            stat_label = QLabel(inner_dict['stat'])
            value_label = QLabel(f"+{inner_dict['value']}")
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(lambda state, stat=inner_dict['stat'], value=inner_dict['value']:
                                          self.on_checkbox_changed(state, stat, value))
            self.grid.addWidget(name_label, row, 0)
            self.grid.addWidget(stat_label, row, 1)
            self.grid.addWidget(value_label, row, 2)
            self.grid.addWidget(checkbox, row, 3)
            row += 1

        #self.widget.show()
        #self.scroll_area.show()
        self.sub_button.clicked.connect(self.sub_on_click)
        #self.calculate_button.clicked.connect(self.calculate_on_click)
        self.label1.setText(self.label1_text)
        self.label2.setText(self.label2_text)
        self.label3.setText(self.label3_text)
        self.label1_2.setText(str(self.label1_2_text))
        self.label2_2.setText(str(self.label2_2_text))
        self.label3_2.setText(str(self.label3_2_text))
        self.sub_ui = None

    def sub_on_click(self):
        self.hide()
        self.sub_ui = sub.SubWindow(self)
        self.sub_ui.show()
        self.sub_ui.closed.connect(self.show_main_ui)

    def on_checkbox_changed(self, state, stat, value):
        if state:
            if stat == 'Strength':
                self.label1_2_text += value
            elif stat == 'Defense':
                self.label2_2_text += value
            elif stat == 'Magic':
                self.label3_2_text += value
        else:
            if stat == 'Strength':
                self.label1_2_text -= value
            elif stat == 'Defense':
                self.label2_2_text -= value
            elif stat == 'Magic':
                self.label3_2_text -= value
        self.label1_2.setText(str(self.label1_2_text))
        self.label2_2.setText(str(self.label2_2_text))
        self.label3_2.setText(str(self.label3_2_text))

    def show_main_ui(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    app.exec()
