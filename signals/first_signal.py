import sys
from tabnanny import check

from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal")

        button = QPushButton("Press me!")
        
        # Make the button "checkable" — it can stay pressed (toggle behavior)
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
