import sys
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    btnPressed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("???")

        self.btn = QPushButton("Press me!")
        self.setCentralWidget(self.btn)

        self.btn.pressed.connect(self.pres)
        self.btnPressed.connect(self.change)

    @pyqtSlot()
    def pres(self):
        self.btnPressed.emit(True)

    @pyqtSlot(bool)
    def change(self):
        self.setWindowTitle("PRESSED!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()