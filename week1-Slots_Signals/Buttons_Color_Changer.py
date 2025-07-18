import sys
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QHBoxLayout, QWidget
)

class Color(QObject):

    ShowResult = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.colors_list = []

    def color_info(self, new_color):
        self.colors_list.append(new_color)
        self.ShowResult.emit(self.colors_list)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change button's color")

        self.line = QLineEdit()
        self.line.setPlaceholderText("Type colour name here")
        self.btn = QPushButton("Change!")
        self.lab = QLabel("No colors used..")

        self.color = Color()
        self.color.ShowResult.connect(self.show_changes)
        self.btn.clicked.connect(self.get_info)

        lay = QHBoxLayout()
        lay.addWidget(self.line)
        lay.addWidget(self.btn)
        lay.addWidget(self.lab)

        center = QWidget()
        center.setLayout(lay)
        self.setCentralWidget(center)

    def get_info(self):
        new_color = self.line.text()
        self.color.color_info(new_color)

    def show_changes(self, colors_list):
        show_color = self.color.colors_list[-1]
        self.btn.setStyleSheet(f"background-color: {show_color};")
        self.lab.setText(f"Used colors: {', '.join(self.color.colors_list)}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
