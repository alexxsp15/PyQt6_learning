import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StoringData")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)

        self.button_is_checked = False
        self.button.setChecked(self.button_is_checked)

        self.button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(self.button)

    def the_button_was_toggled(self, checked):
        # Update internal state when the button is toggled
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
