import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit...")

        mainlay = QVBoxLayout()

        self.line = QLineEdit()
        mainlay.addWidget(self.line)

        btnslay = QHBoxLayout()
        self.bntReadOnly = QPushButton("Make Read Only")
        self.btnEchoMode = QPushButton("Secret!!")
        self.confirmbtn = QPushButton("Confirm")
        self.clearbtn = QPushButton("Clear!")

        btnslay.addWidget(self.confirmbtn)
        btnslay.addWidget(self.btnEchoMode)
        btnslay.addWidget(self.bntReadOnly)
        btnslay.addWidget(self.clearbtn)


        self.confirmbtn.clicked.connect(self.confirm)
        self.btnEchoMode.clicked.connect(self.password)
        self.bntReadOnly.clicked.connect(self.read)
        self.clearbtn.clicked.connect(self.clear)


        mainlay.addLayout(btnslay)

        # Label
        self.lab = QLabel("nothing here..")
        mainlay.addWidget(self.lab)

        central_widget = QWidget()
        central_widget.setLayout(mainlay)
        self.setCentralWidget(central_widget)

    def confirm(self):
        txt = self.line.text()
        self.lab.setText(txt)

    def read(self):
        a = self.line.isReadOnly()
        if a:
            self.line.setReadOnly(False)
        else: self.line.setReadOnly(True)

    def password(self):
        mode = self.line.echoMode()
        if mode == QLineEdit.EchoMode.Normal:
            self.line.setEchoMode(QLineEdit.EchoMode.Password)
        elif mode == QLineEdit.EchoMode.Password:
            self.line.setEchoMode(QLineEdit.EchoMode.Normal)

    def clear(self):
        self.line.clear()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
