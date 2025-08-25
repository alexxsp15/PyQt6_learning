import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QBrush, QPainterPath, QPen, QLinearGradient
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)

        brush = QBrush(QColor("green"), Qt.BrushStyle.HorPattern)

        path = QPainterPath()
        path.arcMoveTo(20, 70, 220, 200, 0)
        path.arcTo(20, 70, 220, 200, 0, 180)
        path.lineTo(240, 430)
        path.lineTo(460, 170)
        path.arcMoveTo(240, 70, 220, 200, 0)
        path.arcTo(240, 70, 220, 200, 0, 180)

        #grad = QLinearGradient(20, 250, 460, 250)
        #grad.setColorAt(0.0, QColor("green"))
        #grad.setColorAt(1.0, QColor("red"))
        #brush = QBrush(grad)

        painter.fillPath(path, brush)

        #painter.drawArc(10, 10, 230, 200, 0 * 16, 180 * 16)
        #painter.drawArc(240, 10, 230, 200, 0 * 16, 180 * 16)
        #painter.drawLine(10, 110, 250, 490)
        #painter.drawLine(250, 490, 470, 110)

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
