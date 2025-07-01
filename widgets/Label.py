import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label")

        #create a winget QLabel
        #Label, text in ()
        widget = QLabel("I'm Alex!")

        #we can change its text:   setText
        widget.setText("I'm from Ukraine!")

        #we can change font:
        font = widget.font()
          #change its size    .setPointSize
        font.setPointSize(80)
          #chenge font        .setFamily
        font.setFamily("Times New Roman")
          #applying changes
        widget.setFont(font)

        #The alignment         .setAlignment     Qt.AlignmentFlag
        widget.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        #set that widget in the center
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()