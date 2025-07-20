from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import sys

class MyButton(QPushButton):
    def mousePressEvent(self, event):
        print("PRESSED!")
        super().mousePressEvent(event)  #DON'T FORGET PARENT METHOD!!

    def mouseReleaseEvent(self, event):
        print("BYEEE!!!")
        super().mouseReleaseEvent(event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Tracking Example")
        self.resize(500, 500)

        lay = QVBoxLayout()

        self.btn = MyButton("Натисни мене")
        lay.addWidget(self.btn)

        self.setLayout(lay)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
