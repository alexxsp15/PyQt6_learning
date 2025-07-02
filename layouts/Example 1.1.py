import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QStackedLayout, QPushButton, QWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Example 1 - choose color")

        mainlayout = QHBoxLayout()

        buttonLayout = QVBoxLayout()
        buttonLayout.setSpacing(0)
        
        self.colorsLayout = QStackedLayout()

        mainlayout.addLayout(buttonLayout)
        mainlayout.addLayout(self.colorsLayout)

        btn1 = QPushButton("green")
        btn1.pressed.connect(self.green_bnt_pushed)
        buttonLayout.addWidget(btn1)
        self.colorsLayout.addWidget(Color("green"))

        btn2 = QPushButton("red")
        btn2.pressed.connect(self.red_bnt_pushed)
        buttonLayout.addWidget(btn2)
        self.colorsLayout.addWidget(Color("red"))

        btn3 = QPushButton("black")
        btn3.pressed.connect(self.black_bnt_pushed)
        buttonLayout.addWidget(btn3)
        self.colorsLayout.addWidget(Color("black"))

        centralWidget = QWidget()
        centralWidget.setLayout(mainlayout)
        self.setCentralWidget(centralWidget)

    def green_bnt_pushed(self):
        self.colorsLayout.setCurrentIndex(0)

    def red_bnt_pushed(self):
        self.colorsLayout.setCurrentIndex(1)

    def black_bnt_pushed(self):
        self.colorsLayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
