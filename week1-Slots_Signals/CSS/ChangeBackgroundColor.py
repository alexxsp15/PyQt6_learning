import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change my color!")

        self.resize(200, 100)

        self.line = QLineEdit()
        self.btn = QPushButton("Change!")
        self.lab = QLabel()

        self.btn.clicked.connect(self.change_color)

        lay = QVBoxLayout()
        lay.addWidget(self.line)
        lay.addWidget(self.btn)
        lay.addWidget(self.lab)

        self.central_widget = QWidget()
        self.central_widget.setLayout(lay)
        self.setCentralWidget(self.central_widget)

        self.line.setStyleSheet("""
        QLineEdit {
        color: black;
        background-color: grey;
        border: 3px dotted;
        border-radius: 0px;
        padding: 4px;
        font-size: 30px;
        selection-background-color: red;
        selection-color: green;
        font-family: Times New Roman;
        }
        
        QLineEdit:focus {
        background-color: white;
        border: 3px dotted;
        }
        """)

        self.btn.setStyleSheet("""
        QPushButton {
        background-color: purple;
        color: white;
        border: 3px solod purple;
        border-radius: 2px;
        font-size: 15px;
        font-weight: bold;
        }
        
        QPushButton:hover {
        background-color: grey;
        }
        
        QPushButton:pressed {
        background-color: black
        }""")

        self.lab.setStyleSheet("""
        QLabel {
        color: black;
        background-color: white;
        border: 2px solid yellow;
        }""")

    def change_color(self):
        color = self.line.text()
        self.central_widget.setStyleSheet(f"background-color: {color};")
        self.lab.setText(f"Current color: {color}!")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()