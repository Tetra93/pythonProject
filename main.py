import os.path
import random
import sys
import json
import sub
from PyQt6.QtWidgets import (QMainWindow, QApplication, QPushButton,
                             QLabel, QScrollArea, QCheckBox, QWidget,
                             QGridLayout, QComboBox, QHBoxLayout)
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
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
    images_path = os.path.join(os.path.dirname(__file__), 'images')
    icons_path = os.path.join(images_path, 'icons')
    icons_list = os.listdir(icons_path)
    heart_path = os.path.join(images_path, 'heart2.png')
    sub_button: QPushButton
    calculate_button: QPushButton
    race_box: QComboBox
    gender_box: QComboBox
    weapon_box: QComboBox
    main_armor_box: QComboBox
    sub_armor_box: QComboBox
    accessory_box: QComboBox
    hearts: QHBoxLayout
    command_slots: QHBoxLayout
    heart1: QLabel
    strength_label: QLabel
    defense_label: QLabel
    magic_label: QLabel
    status_resistances = {'Resist Fire': 0, 'Resist Ice': 0, 'Resist Lightning': 0, 'Resist Slow': 0,
                          'Resist Stop': 0, 'Resist Poison': 0, 'Resist Curse': 0, 'Resist Stone': 0}
    artifact_strength = 0
    artifact_defense = 0
    artifact_magic = 0
    health = 4
    slots = 4
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
        hearts = self.findChild(QHBoxLayout, 'hearts')
        self.race_box.addItems(['Clavat', 'Selkie', 'Lilty', 'Yuke'])
        self.gender_box.addItems((['Male', 'Female']))
        #self.accessory_box.addItem('None')
        #for key, inner_dict in self.accessories.items():
        #    self.accessory_box.addItems([key])
        self.race_box.currentTextChanged.connect(self.race_changed)
        self.gender_box.currentTextChanged.connect(self.gender_changed)
        self.populate_weapons()
        self.weapon_box.currentTextChanged.connect(self.weapon_changed)
        self.populate_main_armor()
        self.main_armor_box.currentTextChanged.connect(self.main_armor_changed)
        self.populate_sub_armor()
        self.sub_armor_box.currentTextChanged.connect(self.sub_armor_changed)
        self.populate_accessories()
        self.accessory_box.currentTextChanged.connect(self.accessory_changed)
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
        self.command_slots.itemAt(0).widget().setPixmap(
            QPixmap(os.path.join(self.icons_path, "sword.png")).scaled(22, 20))
        self.command_slots.itemAt(1).widget().setPixmap(
            QPixmap(os.path.join(self.images_path, "shield.png")).scaled(22, 20))
        self.command_slots.itemAt(2).widget().setPixmap(
            QPixmap(os.path.join(self.icons_path, f"{random.choice(self.icons_list)}")).scaled(22, 20))
        self.command_slots.itemAt(3).widget().setPixmap(
            QPixmap(os.path.join(self.icons_path, f"{random.choice(self.icons_list)}")).scaled(22, 20))

        self.race_changed()
        self.gender_changed()
        self.weapon_changed()
        self.main_armor_changed()
        self.sub_armor_changed()
        self.total_health()
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

    def populate_main_armor(self):
        for key, inner_dict in self.main_armor.items():
            if inner_dict['race'] == self.race_box.currentText() or inner_dict['race'] == 'All':
                self.main_armor_box.addItems([key])

    def populate_sub_armor(self):
        for key, inner_dict in self.sub_armor.items():
            if inner_dict['race'] == self.race_box.currentText():
                self.sub_armor_box.addItems([key])

    def populate_accessories(self):
        self.accessory_box.addItem('None')
        for key, inner_dict in self.accessories.items():
            if inner_dict['race'] == self.race_box.currentText() or inner_dict['race'] == "All":
                if inner_dict['gender'] == self.gender_box.currentText() or inner_dict['gender'] == 'All':
                    self.accessory_box.addItems([key])

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
        self.main_armor_box.clear()
        self.sub_armor_box.clear()
        self.accessory_box.clear()
        self.populate_weapons()
        self.populate_main_armor()
        self.populate_sub_armor()
        self.populate_accessories()
        self.total_stats()

    def gender_changed(self):
        self.accessory_box.clear()
        self.populate_accessories()

    def weapon_changed(self):
        if self.weapon_box.currentText() != '':
            self.weapon_strength = int(self.weapons[self.weapon_box.currentText()]['Strength'])
            self.total_stats()
        else:
            self.weapon_strength = 0
            self.total_stats()

    def main_armor_changed(self):
        if self.main_armor_box.currentText() != '':
            self.main_defense = int(self.main_armor[self.main_armor_box.currentText()]['Defense'])
            self.total_stats()
            if self.main_armor[self.main_armor_box.currentText()]['effect'] is not None:
                self.total_resistances()
        else:
            self.main_defense = 0
            self.total_stats()

    def sub_armor_changed(self):
        if self.sub_armor_box.currentText() != '':
            self.sub_defense = int(self.sub_armor[self.sub_armor_box.currentText()]['Defense'])
            self.total_stats()
            if self.sub_armor[self.sub_armor_box.currentText()]['effect'] is not None:
                self.total_resistances()
        else:
            self.sub_defense = 0
            self.total_stats()

    def accessory_changed(self):
        print('Hello')

    def on_checkbox_changed(self, state, stat, value):
        if state:
            if stat == 'Strength':
                self.artifact_strength += value
            elif stat == 'Defense':
                self.artifact_defense += value
            elif stat == 'Magic':
                self.artifact_magic += value
            elif stat == 'Health':
                self.health += value
                self.total_health()
            elif stat == 'Slots':
                self.slots += value
                self.total_slots()
        else:
            if stat == 'Strength':
                self.artifact_strength -= value
            elif stat == 'Defense':
                self.artifact_defense -= value
            elif stat == 'Magic':
                self.artifact_magic -= value
            elif stat == 'Health':
                self.health -= value
                self.total_health()
            elif stat == 'Slots':
                self.slots -= value
                self.total_slots()
        self.total_stats()
        
    def total_stats(self):
        strength = (self.artifact_strength + self.race_strength + self.weapon_strength)
        defense = (self.artifact_defense + self.race_defense + self.main_defense + self.sub_defense)
        magic = (self.artifact_magic + self.race_magic)
        for key in self.status_resistances:
            self.status_resistances[key] = 0
        if self.main_armor_box.count() > 0:
            if self.main_armor[self.main_armor_box.currentText()]['effect'] is not None:
                self.status_resistances[self.main_armor[self.main_armor_box.currentText()]['effect']] \
                    += self.main_armor[self.main_armor_box.currentText()]['value']
                for key in self.status_resistances:
                    print(self.status_resistances[key])
        self.strength_label.setText(str(strength))
        self.defense_label.setText(str(defense))
        self.magic_label.setText(str(magic))

    def total_resistances(self):
        for key in self.status_resistances:
            self.status_resistances[key] = 0
        if self.main_armor_box.count() > 0:
            if self.main_armor[self.main_armor_box.currentText()]['effect'] is not None:
                self.status_resistances[self.main_armor[self.main_armor_box.currentText()]['effect']] \
                    += self.main_armor[self.main_armor_box.currentText()]['value']
        if self.sub_armor_box.count() > 0:
            if self.sub_armor[self.sub_armor_box.currentText()]['effect'] is not None:
                self.status_resistances[self.sub_armor[self.sub_armor_box.currentText()]['effect']] \
                    += self.sub_armor[self.sub_armor_box.currentText()]['value']
        for key in self.status_resistances:
            print(self.status_resistances[key])

    def total_health(self):
        for i in range(self.hearts.count()):
            if i <= (self.health - 1):
                self.hearts.itemAt(i).widget().setPixmap(QPixmap(self.heart_path).scaled(22, 20))
            else:
                self.hearts.itemAt(i).widget().setPixmap(QPixmap())

    def total_slots(self):
        for i in range(4, self.command_slots.count()):
            if self.command_slots.itemAt(i).widget().pixmap().isNull() and i <= (self.slots - 1):
                self.command_slots.itemAt(i).widget().setPixmap(QPixmap(
                    os.path.join(self.icons_path, f"{random.choice(self.icons_list)}")).scaled(22, 20))
            elif i > (self.slots - 1):
                self.command_slots.itemAt(i).widget().setPixmap(QPixmap())

    def show_main_ui(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    app.exec()
