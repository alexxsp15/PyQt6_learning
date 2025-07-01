import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")

        widget = QComboBox()
        widget.addItems(["Alex", "Yana", "Alina"])

        #now we can edit data in the box
        widget.setEditable(True)

        #and we can set policy for that data
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)

        #sends the current index (position) of the selected item
        widget.currentIndexChanged.connect(self.index_changed)

        #there is an alternate signal to send the text
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()