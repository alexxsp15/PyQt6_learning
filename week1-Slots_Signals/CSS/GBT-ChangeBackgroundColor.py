import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change my color!")
        self.resize(400, 200)

        self.line = QLineEdit()
        self.btn = QPushButton("Change!")
        self.lab = QLabel("Current color: -")

        self.lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lab.setFixedHeight(40)

        self.btn.clicked.connect(self.change_color)

        lay = QVBoxLayout()
        lay.addWidget(self.line)
        lay.addWidget(self.btn)
        lay.addWidget(self.lab)

        self.central_widget = QWidget()
        self.central_widget.setLayout(lay)
        self.setCentralWidget(self.central_widget)

        # Стилі
        self.line.setStyleSheet("""
        QLineEdit {
            color: black;
            background-color: grey;
            border: 3px dotted;
            border-radius: 0px;
            padding: 4px;
            font-size: 24px;
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
            border: 3px solid purple;
            border-radius: 4px;
            font-size: 18px;
            font-weight: bold;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: grey;
        }
        QPushButton:pressed {
            background-color: black;
        }
        """)

        self.lab.setStyleSheet("""
        QLabel {
            color: black;
            background-color: white;
            border: 2px solid yellow;
            font-size: 20px;
        }
        """)

    def change_color(self):
        color = self.line.text()
        self.central_widget.setStyleSheet(f"background-color: {color};")
        self.lab.setText(f"Current color: {color}!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
