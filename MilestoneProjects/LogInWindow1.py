import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log in")

        widget = QWidget()
        widget.setFixedSize(450, 550)
        widget.setStyleSheet("""
        QWidget {
        background-color: #189ab4;
        border-radius: 40px;
        }""")

        topLabel = QLabel("Log in")
        topLabel.setStyleSheet("""
        QLabel {
        color: #d4f1f4;
        font-size: 60px;
        font-weight: bold;
        }""")

        logLab = QLabel("Enter your log in:")
        logLab.setStyleSheet("""
        QLabel {
        color: #d4f1f4;
        font-size: 35px;
        }""")

        loginLine = QLineEdit()

        loginLine.setStyleSheet("""
        QLineEdit {
        background-color: #75e6da;
        border: 2px;
        border-radius: 6px;
        font-size: 30px;
        }""")
        loginLine.setMaximumWidth(350)

        reglab = QLabel("Enter your password:")
        reglab.setStyleSheet("""
                QLabel {
                color: #d4f1f4;
                font-size: 35px;
                }""")


        passwordLine = QLineEdit()
        passwordLine.setStyleSheet("""
                QLineEdit {
                background-color: #75e6da;
                border: 2px;
                border-radius: 6px;
                font-size: 30px;
                }""")
        passwordLine.setMaximumWidth(350)

        button = QPushButton("OK")
        button.setStyleSheet("""
        QPushButton {
            background-color: #05445e;
            color: #d4f1f4;
            font-size: 30px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #033b4a;
        }
        """)

        button.setFixedHeight(60)
        button.setMaximumWidth(170)

        contenlayout = QVBoxLayout()
        contenlayout.setSpacing(5)
        contenlayout.setContentsMargins(40, 40, 40, 40)

        contenlayout.addWidget(topLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        contenlayout.addWidget(logLab, alignment=Qt.AlignmentFlag.AlignLeft)
        contenlayout.addWidget(loginLine, alignment=Qt.AlignmentFlag.AlignTop)
        contenlayout.addWidget(reglab, alignment=Qt.AlignmentFlag.AlignLeft)
        contenlayout.addWidget(passwordLine, alignment=Qt.AlignmentFlag.AlignTop)
        contenlayout.addWidget(button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(contenlayout)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)

        mainWidget = QWidget()
        mainWidget.setStyleSheet("background-color: #05445e;")
        mainWidget.setLayout(mainlayout)

        self.setCentralWidget(mainWidget)
        self.showMaximized()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()