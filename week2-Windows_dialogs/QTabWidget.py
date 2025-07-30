import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QTabWidget, QVBoxLayout

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: green;")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setStyleSheet("background-color: white;")

        layout.addWidget(self.btn1)
        self.setLayout(layout)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setStyleSheet("background-color: white;")

        layout.addWidget(self.btn1)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("background-color: blue;")

        self.tab1 = Page1()
        self.tab2 = Page2()

        self.tabs.addTab(self.tab1, "page1")
        self.tabs.addTab(self.tab2, "page2")

        self.tabs.currentChanged.connect(self.tab_changed)

        self.setCentralWidget(self.tabs)

    def tab_changed(self, index):
        if index == 0:
            self.tabs.setStyleSheet("background-color: blue;")
        elif index == 1:
            self.tabs.setStyleSheet("background-color: green;")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()