import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDockWidget, QVBoxLayout, QHBoxLayout, QListWidget, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dock")

        but = QPushButton("Press me!")
        but.clicked.connect(self.butcl)


        dock = QDockWidget()
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        list = QListWidget()

        lay = QHBoxLayout()
        lay.addWidget(but)
        dock.setWidget(list)
        lay.addWidget(dock)

        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)

    def butcl(self):
        pass







app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()