import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        self.TitleLabel = QLabel("Log in")

        self.LoginLine = QLineEdit()
        self.LoginLine.setPlaceholderText("Enter your email")

        self.PasswordLine = QLineEdit()
        self.PasswordLine.setPlaceholderText("Enter your password")



        MainLayout = QVBoxLayout()
        MainLayout.addWidget(self.TitleLabel)
        MainLayout.addWidget(self.)