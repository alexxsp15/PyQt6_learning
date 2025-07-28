import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QLineEdit, QVBoxLayout, QStackedWidget

class LogInWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program")

        widget = QWidget()
        widget.setFixedSize(450, 600)
        widget.setStyleSheet("background-color: #437057;")

        self.TopLabel = QLabel("Log in")
        self.TopLabel.setStyleSheet("""
        QLabel {
        color: #E3DE61;
        font-size: 80px;
        font-weight: bold;
        }""")

        self.LogLabel = QLabel("Enter your login:")
        self.LogLabel.setStyleSheet("""
        QLabel {
        color: #E3DE61;
        font-size: 35px;
        }""")

        self.LogLine = QLineEdit()
        self.LogLine.setStyleSheet("""
        QLineEdit {
        color: #E7EFC7;
        background-color: #97B067;
        font-size: 25px;
        border: 3px;
        border-radius: 5px;
        }""")
        self.LogLine.setMaximumWidth(370)

        self.PasswordLabel = QLabel("Enter your password:")
        self.PasswordLabel.setStyleSheet("""
                QLabel {
                color: #E3DE61;
                font-size: 35px;
                }""")

        self.PasswordLine = QLineEdit()
        self.PasswordLine.setStyleSheet("""
                QLineEdit {
                color: #E7EFC7;
                background-color: #97B067;
                font-size: 25px;
                border: 3px;
                border-radius: 5px;
                }""")
        self.PasswordLine.setMaximumWidth(370)
        self.PasswordLine.setEchoMode(QLineEdit.EchoMode.Password)

        self.button = QPushButton("OK")
        self.button.setStyleSheet("""
        QPushButton {
        color: #437057;
        background-color: #97B067;
        border: 5px;
        border-radius: 2px;
        }""")
        self.button.setFixedHeight(60)
        self.button.setMaximumWidth(170)

        layout = QVBoxLayout()
        layout.addWidget(self.TopLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.LogLabel, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.LogLine, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.PasswordLabel, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.PasswordLine, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignBottom)

        widget.setLayout(layout)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter)
        self.setLayout(mainlayout)

        self.showMaximized()


class GreetingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello!")

        self.greetingLabel = QLabel("Hello!")
        self.GoBackButton = QPushButton("Log out")

        layout = QVBoxLayout()
        layout.addWidget(self.greetingLabel)
        layout.addWidget(self.GoBackButton)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program")
        self.setStyleSheet("background-color: #2F5249;")

        self.WindowsChanger = QStackedWidget()

        self.login = LogInWindow()
        self.greeting = GreetingWindow()

        self.WindowsChanger.addWidget(self.login)
        self.WindowsChanger.addWidget(self.greeting)

        self.login.button.clicked.connect(self.test)
        self.greeting.GoBackButton.clicked.connect(self.test2)

        self.WindowsChanger.setCurrentIndex(0)

        self.setCentralWidget(self.WindowsChanger)

        self.showMaximized()

    def test(self):
        self.WindowsChanger.setCurrentIndex(1)

    def test2(self):
        self.WindowsChanger.setCurrentIndex(0)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
