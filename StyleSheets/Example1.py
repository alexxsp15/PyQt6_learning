import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ex1")

        lay = QHBoxLayout()

        but = QPushButton("Change color")

        but.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:pressed {
                background-color: red;
                color: black;
                
            }
        """)

        lay.addWidget(but)

        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
