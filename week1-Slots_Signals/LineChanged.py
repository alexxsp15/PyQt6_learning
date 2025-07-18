import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QLabel,
    QVBoxLayout, QWidget
)

class NewText(QObject):
    TextEdit = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def edit(self, text):
        lower_text = text.lower()
        split_text = lower_text.split(".")

        result = []
        for part in split_text:
            part = part.strip()
            if part:
                part = part.capitalize()
                result.append(part)

        final_text = ". ".join(result)
        self.TextEdit.emit(final_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LineChanged")

        self.line = QLineEdit()
        self.lab = QLabel("")

        self.newtext = NewText()

        self.newtext.TextEdit.connect(self.show_text)
        self.line.textChanged.connect(self.get_text)

        lay = QVBoxLayout()
        lay.addWidget(self.line)
        lay.addWidget(self.lab)

        center = QWidget()
        center.setLayout(lay)
        self.setCentralWidget(center)

    def get_text(self):
        text = self.line.text()
        self.newtext.edit(text)

    def show_text(self, text):
        self.lab.setText(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
