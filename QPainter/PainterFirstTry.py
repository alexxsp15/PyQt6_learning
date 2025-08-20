import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("green"), 3, Qt.PenStyle.DashDotLine))
        painter.drawArc(10, 10, 230, 200, 0 * 16, 180 * 16)
        painter.drawArc(240, 10, 230, 200, 0 * 16, 180 * 16)
        painter.drawLine(10, 110, 250, 490)
        painter.drawLine(250, 490, 470, 110)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = MyWidget()
        widget.setFixedSize(500, 500)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
