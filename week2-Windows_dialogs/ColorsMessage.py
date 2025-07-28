import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QDialog,
    QMessageBox, QPushButton, QMainWindow, QVBoxLayout
)

class MyDialog(QDialog):
    mySignal = pyqtSignal(bool)

    def __init__(self, expected_color):
        super().__init__()
        self.setWindowTitle("Processing...")

        self.expected = expected_color

        self.label = QLabel("Re-enter your color below:")
        self.line = QLineEdit()
        self.button = QPushButton("Check")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.checking)

    def checking(self):
        entered = self.line.text().strip()
        if entered.lower() == self.expected.lower():
            self.mySignal.emit(True)
            self.accept()
        else:
            self.mySignal.emit(False)
            self.reject()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Chooser")

        self.line = QLineEdit()
        self.btn = QPushButton("I want this color")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter a color (e.g. red, #ff0000):"))
        layout.addWidget(self.line)
        layout.addWidget(self.btn)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        color = self.line.text().strip()
        if not color:
            QMessageBox.warning(self, "Warning", "Please enter a color!")
            return

        dialog = MyDialog(color)
        dialog.mySignal.connect(lambda match: self.after_check(match, color))
        dialog.exec()

    def after_check(self, match, color):
        if match:
            reply = QMessageBox.question(
                self,
                "Confirm",
                f"Are you sure you want this color: {color}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.showres(color)
        else:
            QMessageBox.critical(self, "Mismatch", "Color entries do not match.")

    def showres(self, color):
        self.setStyleSheet(f"background-color: {color};")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
