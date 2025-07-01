import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ListWidget")

        widget = QListWidget()
        widget.addItems(["Alex", "Yana", "Alina", "Alex", "Yana", "Alina", "Alex", "Yana", "Alina","Alex", "Yana", "Alina"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
