import random
import sys
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton


class MainWindow(QMainWindow):
    colorPick = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RandomColor")

        self.btn = QPushButton("Change my color!")
        self.setCentralWidget(self.btn)

        self.btn.pressed.connect(self.click)
        self.colorPick.connect(self.changer)

    @pyqtSlot()
    def click(self):
        self.a = random.randint(1, 225)
        self.b = random.randint(1, 225)
        self.c = random.randint(1, 225)
        self.colorPick.emit(self.a, self.b, self.c)

    @pyqtSlot(int, int, int)
    def changer(self, a, b, c):
        self.color = QColor(a, b, c)
        self.btn.setStyleSheet(f"background-color: {self.color.name()};")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
