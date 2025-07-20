import sys
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QWidget
)

class Word(QObject):
    CurrentProgress = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.wordlist = ['p', 'y', 't', 'h', 'o', 'n']
        self.to_send_info = ['*'] * len(self.wordlist)
        self.guesses_counter = 9
        self.guessed_letters = set()

    def check_letter(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            self.CurrentProgress.emit(["Already guessed!"])
            return

        self.guessed_letters.add(letter)
        found = False

        for i, ch in enumerate(self.wordlist):
            if ch == letter and self.to_send_info[i] == '*':
                self.to_send_info[i] = letter
                found = True

        if found:
            self.CurrentProgress.emit(self.to_send_info)
        else:
            self.guesses_counter -= 1
            self.CurrentProgress.emit(["WRONG!"])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guess my word!")

        self.lab = QLabel(" ".join(['*'] * 6))
        self.lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.line = QLineEdit()
        self.line.setMaxLength(1)
        self.line.setPlaceholderText("Enter a letter...")

        self.btn = QPushButton("GUESS")

        self.message = QLabel("")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.glab = QLabel("You have 9 guesses left!")
        self.glab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.word = Word()
        self.word.CurrentProgress.connect(self.show_result)
        self.btn.clicked.connect(self.get_info)

        layout = QVBoxLayout()
        layout.addWidget(self.lab)
        layout.addWidget(self.line)
        layout.addWidget(self.btn)
        layout.addWidget(self.message)
        layout.addWidget(self.glab)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_info(self):
        letter = self.line.text().strip()
        self.line.clear()

        if not letter.isalpha() or len(letter) != 1:
            self.message.setText("Enter one letter only.")
            return

        self.word.check_letter(letter)

    def show_result(self, result):
        if result == ["Already guessed!"]:
            self.message.setText("You already guessed that letter.")
        elif result == ["WRONG!"]:
            self.message.setText("Wrong guess!")
        else:
            self.message.setText("Good job!")
            self.lab.setText(" ".join(result))

        guesses_left = self.word.guesses_counter
        self.glab.setText(f"You have {guesses_left} guesses left.")

        if guesses_left == 0:
            self.message.setText("You ran out of guesses!")
            self.lab.setText(" ".join(self.word.wordlist))
            self.line.setReadOnly(True)
            self.btn.setEnabled(False)

        if "*" not in self.word.to_send_info:
            self.message.setText("Congratulations! You guessed the word!")
            self.line.setReadOnly(True)
            self.btn.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
