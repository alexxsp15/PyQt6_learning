import sys
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    numChanged = pyqtSignal(int)  

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter")

        self.n = 0

        lay = QVBoxLayout()

        self.btn = QPushButton("+1")
        self.btn.pressed.connect(self.plusone)

        self.numChanged.connect(self.changer)
        self.lab = QLabel("0")

        lay.addWidget(self.btn)
        lay.addWidget(self.lab)

        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def plusone(self):
        self.n += 1
        self.numChanged.emit(self.n)

    @pyqtSlot(int)
    def changer(self, n):
        self.lab.setText(str(n))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
