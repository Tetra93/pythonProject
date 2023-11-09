import sys
import json

from PyQt6.QtWidgets import (QMainWindow, QApplication, QPushButton,
                             QLabel, QScrollArea, QCheckBox, QWidget, QGridLayout, QComboBox)
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal

import sub
from sub import SubWindow


class MainUI(QMainWindow):
    with open('items.txt', 'r') as file:
        data = json.load(file)

    #artifacts_unsorted = data[0]
    artifacts = sorted(data[0].items(), key=lambda x: (x[1]['stat'], x[1]['value']))
    sub_button: QPushButton
    calculate_button: QPushButton
    comboBox: QComboBox
    label1: QLabel
    label2: QLabel
    label3: QLabel
    label1_2: QLabel
    label2_2: QLabel
    label3_2: QLabel
    label1_text = 'Strength'
    label2_text = 'Defense'
    label3_text = 'Magic'
    artifact_strength = 0
    artifact_defense = 0
    artifact_magic = 0
    race_strength = 0
    race_defense = 0
    race_magic = 0
    equip_strength = 0
    equip_defense = 0

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("mainWindow.ui", self)

        self.comboBox.addItems(['Clavat', 'Selkie', 'Lilty', 'Yuke'])
        self.comboBox.currentTextChanged.connect(self.race_changed)
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(60, 10, 330, 180)
        self.grid = QGridLayout(self.widget)
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(60, 10, 330, 180)
        self.scroll_area.setWidget(self.widget)
        row = 0
        for key, inner_dict in self.artifacts:
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

        self.sub_button.clicked.connect(self.sub_on_click)
        self.label1.setText(self.label1_text)
        self.label2.setText(self.label2_text)
        self.label3.setText(self.label3_text)
        self.race_changed()
        self.sub_ui = None

    def sub_on_click(self):
        self.hide()
        self.sub_ui = sub.SubWindow(self)
        self.sub_ui.show()
        self.sub_ui.closed.connect(self.show_main_ui)

    def race_changed(self):
        race = self.comboBox.currentText()
        if race == 'Clavat':
            self.race_strength = 8
            self.race_defense = 7
            self.race_magic = 13
        elif race == 'Selkie':
            self.race_strength = 7
            self.race_defense = 6
            self.race_magic = 12
        elif race == 'Lilty':
            self.race_strength = 8
            self.race_defense = 8
            self.race_magic = 10
        elif race == 'Yuke':
            self.race_strength = 5
            self.race_defense = 5
            self.race_magic = 15

        self.total_stats()

    def on_checkbox_changed(self, state, stat, value):
        if state:
            if stat == 'Strength':
                self.artifact_strength += value
            elif stat == 'Defense':
                self.artifact_defense += value
            elif stat == 'Magic':
                self.artifact_magic += value
        else:
            if stat == 'Strength':
                self.artifact_strength -= value
            elif stat == 'Defense':
                self.artifact_defense -= value
            elif stat == 'Magic':
                self.artifact_magic -= value
        self.total_stats()
        
    def total_stats(self):
        strength = (self.artifact_strength + self.race_strength + self.equip_strength)
        defense = (self.artifact_defense + self.race_defense + self.equip_defense)
        magic = (self.artifact_magic + self.race_magic)
        self.label1_2.setText(str(strength))
        self.label2_2.setText(str(defense))
        self.label3_2.setText(str(magic))

    def show_main_ui(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    app.exec()
