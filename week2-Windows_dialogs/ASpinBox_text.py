import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QSpinBox, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SpinBox Example")

        self.lab = QLabel("idk how old are u..")
        self.spin = QSpinBox()

        self.spin.setRange(0, 120)
        self.spin.editingFinished.connect(self.update_label)

        layout = QVBoxLayout()
        layout.addWidget(self.lab)
        layout.addWidget(self.spin)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self):
        y = self.spin.cleanText()
        self.lab.setText(f"mkay ur {y} yo.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
