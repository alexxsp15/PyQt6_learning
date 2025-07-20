from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
import sys


class TrackingWidget(QWidget):
    def __init__(self, color, name):
        super().__init__()
        self.setStyleSheet(f"background-color: {color};")
        self.name = name
        self.setMouseTracking(True)

    def enterEvent(self, event):
        print(f"➡ Курсор ЗАЙШОВ у {self.name}")
        return super().enterEvent(event)

    def leaveEvent(self, event):
        print(f"⬅ Курсор ВИЙШОВ з {self.name}")
        return super().leaveEvent(event)

    def mouseMoveEvent(self, event):
        pos = event.position()
        print(f"🖱 Курсор РУХАЄТЬСЯ у {self.name}: x={pos.x()}, y={pos.y()}")
        return super().mouseMoveEvent(event)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Tracking Example")
        self.resize(400, 400)

        layout = QVBoxLayout()

        red_widget = TrackingWidget("lightcoral", "RedWidget")
        green_widget = TrackingWidget("lightgreen", "GreenWidget")
        blue_widget = TrackingWidget("lightblue", "BlueWidget")

        layout.addWidget(red_widget)
        layout.addWidget(green_widget)
        layout.addWidget(blue_widget)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
