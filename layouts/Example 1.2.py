import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Example 2")

        btn_layout = QHBoxLayout()
        self.colours_layout = QStackedLayout()
        main_layout = QVBoxLayout()

        btn1 = QPushButton("white")
        btn1.clicked.connect(self.white_btn)
        btn_layout.addWidget(btn1)
        self.colours_layout.addWidget(Color("white"))

        btn2 = QPushButton("grey")
        btn2.clicked.connect(self.grey_btn)
        btn_layout.addWidget(btn2)
        self.colours_layout.addWidget(Color("grey"))

        btn3 = QPushButton("black")
        btn3.clicked.connect(self.black_btn)
        btn_layout.addWidget(btn3)
        self.colours_layout.addWidget(Color("black"))

        main_layout.addLayout(btn_layout)
        main_layout.addLayout(self.colours_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def white_btn(self):
        self.colours_layout.setCurrentIndex(0)

    def grey_btn(self):
        self.colours_layout.setCurrentIndex(1)

    def black_btn(self):
        self.colours_layout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
