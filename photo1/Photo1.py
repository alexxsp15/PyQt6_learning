import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Photo1")

        # creating an object
        widget = QLabel()
        widget.setPixmap(QPixmap('stradew.jpg'))

        widget.setScaledContents(True)
        #widget.setAlignment(Qt.AlignmentFlag.AlignCenter)  # необов'язково, але зручно

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
