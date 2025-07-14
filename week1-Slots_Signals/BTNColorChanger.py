import random
import sys
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton


class MainWindow(QMainWindow):
    colorPick = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.colors = ["red", "blue", "yellow", "black", "green", "white"]

        self.btn = QPushButton("CHANGE ME!!!")
        self.setCentralWidget(self.btn)

        self.btn.pressed.connect(self.press)
        self.colorPick.connect(self.change)

    @pyqtSlot()
    def press(self):
        a = random.choice(self.colors)
        self.colorPick.emit(a)

    @pyqtSlot(str)
    def change(self, a):
        self.btn.setStyleSheet(f"background-color: {a};")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
