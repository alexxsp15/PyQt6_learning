import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel, QPushButton, QWidget, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TEST")

        self.mainWidget = QWidget()
        self.mainWidget.setFixedSize(500, 300)
        self.mainWidget.setStyleSheet("background-color: white")

        self.setCentralWidget(self.mainWidget)

        dock = QDockWidget()
        dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea | Qt.DockWidgetArea.TopDockWidgetArea)

        self.line = QLineEdit()
        self.btn = QPushButton("confirm")

        dockWidget = QWidget()
        dockWidget.setStyleSheet("background-color: grey")

        dockLay = QVBoxLayout()
        dockLay.addWidget(self.line)
        dockLay.addWidget(self.btn)

        self.btn.clicked.connect(self.change)

        dockWidget.setLayout(dockLay)
        dock.setWidget(dockWidget)

        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock)

    def change(self):
        color = self.line.text()
        self.mainWidget.setStyleSheet(f"background-color: {color};")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()