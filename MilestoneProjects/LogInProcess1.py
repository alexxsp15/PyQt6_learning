import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QLineEdit, QVBoxLayout, \
    QStackedWidget, QSizePolicy, QMessageBox


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
            border: 2px solid #437057;
            border-radius: 10px;
            font-size: 24px;
            padding: 10px 30px;
        }
        QPushButton:hover {
            background-color: #A7C077;
        }
        """)
        self.button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(40, 40, 40, 40)

        layout.addWidget(self.TopLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.LogLabel, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.LogLine, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.PasswordLabel, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.PasswordLine, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)

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
        self.greetingLabel.setStyleSheet("""
        QLabel {
        color: #97B067;
        font-size: 100px;
        }""")

        self.GoBackButton = QPushButton("Log out")
        self.GoBackButton.setStyleSheet("""
        QPushButton {
            color: #437057;
            background-color: #97B067;
            border: 2px solid #437057;
            border-radius: 10px;
            font-size: 24px;
            padding: 10px 30px; 
        }
        QPushButton:hover {
            background-color: #A7C077;
        }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.greetingLabel)
        layout.addWidget(self.GoBackButton)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program")
        self.setStyleSheet("background-color: #2F5249;")

        self.user = "alexxsp15"
        self.passw = "idk123"

        self.WindowsChanger = QStackedWidget()

        self.login = LogInWindow()
        self.greeting = GreetingWindow()

        self.WindowsChanger.addWidget(self.login)
        self.WindowsChanger.addWidget(self.greeting)

        self.login.button.clicked.connect(self.log)
        self.greeting.GoBackButton.clicked.connect(self.test2)

        self.WindowsChanger.setCurrentIndex(0)

        self.setCentralWidget(self.WindowsChanger)

        self.showMaximized()

    def log(self):
        currentText = self.login.LogLine.text()
        currentPassword = self.login.PasswordLine.text()
        if currentText == self.user and currentPassword == self.passw:
            QMessageBox.information(self, "Cool!", "Welcome!")
            self.WindowsChanger.setCurrentIndex(1)
            self.login.LogLine.clear()
            self.login.PasswordLine.clear()
        elif currentText != self.user:
            QMessageBox.critical(self, "Error!", "Your username is incorrect!")
        elif currentPassword != self.passw:
            QMessageBox.critical(self, "Error!", "Your password is incorrect!")

    def test2(self):
        self.WindowsChanger.setCurrentIndex(0)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
