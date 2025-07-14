import sys
import random
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):

    textChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextChanger")

        self.lab = QLabel("Hello!")
        self.btn = QPushButton("Change text")

        self.btn.pressed.connect(self.change_text)
        self.textChanged.connect(self.update_label)

        lay = QVBoxLayout()
        lay.addWidget(self.lab)
        lay.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def change_text(self):
        new_text = str(random.random())
        self.textChanged.emit(new_text)

    @pyqtSlot(str)
    def update_label(self, txt):
        self.lab.setText(txt)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
