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

    artifacts = data[0]
    weapons = data[1]
    weapons_filtered = []
    main_armor = data[2]
    sub_armor = data[3]
    accessories = data[4]
    sub_button: QPushButton
    calculate_button: QPushButton
    race_box: QComboBox
    gender_box: QComboBox
    weapon_box: QComboBox
    main_armor_box: QComboBox
    sub_armor_box: QComboBox
    accessory_box: QComboBox
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
    weapon_strength = int(weapons['Copper Sword']['Strength'])
    main_defense = int(main_armor['Travel Clothes']['Defense'])
    sub_defense = int(sub_armor['Makeshift Shield']['Defense'])

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("mainWindow.ui", self)

        row = 0
        self.race_box.addItems(['Clavat', 'Selkie', 'Lilty', 'Yuke'])
        self.gender_box.addItems((['Male', 'Female']))
        for key, inner_dict in self.main_armor.items():
            self.main_armor_box.addItems([key])
        for key, inner_dict in self.sub_armor.items():
            self.sub_armor_box.addItems([key])
        for key, inner_dict in self.accessories.items():
            self.accessory_box.addItems([key])
        self.race_box.currentTextChanged.connect(self.race_changed)
        self.populate_weapons()
        self.weapon_box.currentTextChanged.connect(self.weapon_changed)
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(20, 10, 330, 180)
        self.grid = QGridLayout(self.widget)
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(20, 10, 330, 180)
        self.scroll_area.setWidget(self.widget)
        for key, inner_dict in self.artifacts.items():
            name_label = QLabel(key)
            stat_value = inner_dict['stat']
            if stat_value == 'Other':
                stat_value = 'Magic'
            stat_label = QLabel(stat_value)
            value_label = QLabel(f"+{inner_dict['value']}")
            checkbox = QCheckBox()
            checkbox.stateChanged.connect(lambda state, stat=stat_value, value=inner_dict['value']:
                                          self.on_checkbox_changed(state, stat, value))
            self.grid.addWidget(name_label, row, 0)
            self.grid.addWidget(stat_label, row, 1)
            self.grid.addWidget(value_label, row, 2)
            self.grid.addWidget(checkbox, row, 3)
            row += 1
        self.grid.setColumnStretch(0, 2)
        self.grid.setColumnStretch(1, 2)
        self.grid.setColumnStretch(2, 1)
        self.grid.setColumnStretch(3, 1)
        self.widget.setFixedHeight(self.grid.sizeHint().height())

        self.sub_button.clicked.connect(self.sub_on_click)
        self.label1.setText(self.label1_text)
        self.label2.setText(self.label2_text)
        self.label3.setText(self.label3_text)
        self.race_changed()
        self.weapon_changed()
        self.sub_ui = None

    def sub_on_click(self):
        self.hide()
        self.sub_ui = sub.SubWindow(self)
        self.sub_ui.show()
        self.sub_ui.closed.connect(self.show_main_ui)

    def populate_weapons(self):
        for key, inner_dict in self.weapons.items():
            if self.race_box.currentText() == inner_dict['race']:
                self.weapon_box.addItems([key])

    def race_changed(self):
        race = self.race_box.currentText()
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
        self.weapon_box.clear()
        self.populate_weapons()
        self.total_stats()

    def weapon_changed(self):
        if self.weapon_box.currentText() != '':
            print(self.weapons[self.weapon_box.currentText()])
            self.weapon_strength = int(self.weapons[self.weapon_box.currentText()]['Strength'])
            self.total_stats()
        else:
            self.weapon_strength = 0
            self.total_stats()

    def main_armor_changed(self):
        self.main_defense = int(self.main_armor[self.main_armor_box.currentText()]['Defense'])
        self.total_stats()

    def sub_armor_changed(self):
        self.sub_armor = int(self.sub_armor_box[self.sub_armor_box.currentText()]['Defense'])
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
        strength = (self.artifact_strength + self.race_strength + self.weapon_strength)
        defense = (self.artifact_defense + self.race_defense + self.main_defense + self.sub_defense)
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
