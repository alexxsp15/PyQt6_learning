import random
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import sys


class CounterButton(QPushButton):
    def __init__(self):
        super().__init__("Click me")
        self.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                color: black;
                border: 2px solid gray;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: lightgreen;
            }
        """)
        self.n1 = 0
        self.n2 = 0

    def mousePressEvent(self, e):
        self.n1 += 1
        print(f"Pressed {self.n1}th time")
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.n2 += 1
        print(f"c ya {self.n2}!")
        super().mouseReleaseEvent(e)


class ChangesColor(QPushButton):
    ColorAlert = pyqtSignal(str)

    def __init__(self):
        super().__init__("Змінити колір")
        self.setFixedSize(100, 100)
        self.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 10px solid #c0392b;
                border-radius: 50px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: #34495e;
                color: #1abc9c;
                box-shadow: 0 0 10px #1abc9c;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
                color: #2c3e50;
            }
        """)

        self.color_list = [ "red", "blue", "green", "yellow", "purple", "orange", "pink" ]
        self.color = "white"

        self.clicked.connect(self.send_color)

    def wheelEvent(self, event):
        self.color = random.choice(self.color_list)
        self.setStyleSheet(f"background-color: {self.color};")
        event.accept()

    def send_color(self):
        self.ColorAlert.emit(self.color)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")

        lay = QVBoxLayout()
        self.btn = CounterButton()
        self.btn1 = ChangesColor()

        self.btn1.ColorAlert.connect(self.showres)

        lay.addWidget(self.btn)
        lay.addWidget(self.btn1)
        self.setLayout(lay)

    def showres(self, color):
        print(f"Current color is {color}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
