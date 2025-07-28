import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout

class FirstDialog(QDialog):
    MyChise = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ANSWER!!!")

        self.lab2 = QLabel("are u ok?")
        self.btny = QPushButton("yes")
        self.btnn = QPushButton("nah")

        self.btny.clicked.connect(self.clicked_yes)
        self.btnn.clicked.connect(self.clicked_no)

        dialoglay = QVBoxLayout()
        dialoglay.addWidget(self.lab2)

        btnslay = QHBoxLayout()
        btnslay.addWidget(self.btny)
        btnslay.addWidget(self.btnn)

        dialoglay.addLayout(btnslay)

        self.setLayout(dialoglay)

    def clicked_yes(self):
        self.MyChise.emit("yes")

    def clicked_no(self):
        self.MyChise.emit("no")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("are u okay?")

        self.lab1 = QLabel("U need help..")
        self.btn1 = QPushButton("send help")

        self.mydialog = FirstDialog()

        layout = QVBoxLayout()
        layout.addWidget(self.lab1)
        layout.addWidget(self.btn1)

        self.btn1.clicked.connect(self.clicked_enter)
        self.mydialog.MyChise.connect(self.show_res)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    def clicked_enter(self):
        dialog = FirstDialog()
        dialog.MyChise.connect(self.show_res)
        dialog.exec()

    def show_res(self, answer):
        if answer == "yes":
            self.lab1.setText("LIAR!!!")
        else:
            self.lab1.setText("obv..")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()