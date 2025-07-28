import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QWidget
)

class Pets(QObject):
    AddPet = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.pets_list = []

    def add_pet(self, pet_name: str):
        if pet_name:
            self.pets_list.append(pet_name)
            self.AddPet.emit(self.pets_list)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py Pets!")

        self.line = QLineEdit()
        self.btn = QPushButton("Add pet")
        self.names = QLabel("You don't have any pets..")
        self.count = QLabel("You have 0 pets!")

        self.pets = Pets()

        self.pets.AddPet.connect(self.upd_label)
        self.btn.clicked.connect(self.add_pet)

        layout = QVBoxLayout()
        layout.addWidget(self.line)
        layout.addWidget(self.btn)
        layout.addWidget(self.names)
        layout.addWidget(self.count)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_pet(self):
        pet_name = self.line.text().strip()
        self.pets.add_pet(pet_name)
        self.line.clear()

    def upd_label(self, pets_list):
        if pets_list:
            self.names.setText(f"Your pets: {', '.join(pets_list)}")
            self.count.setText(f"You have {len(pets_list)} pets!")
        else:
            self.names.setText("You don't have any pets..")
            self.count.setText("You have 0 pets!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
