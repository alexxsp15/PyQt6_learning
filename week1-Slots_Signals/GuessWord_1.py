import sys
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QHBoxLayout, QVBoxLayout, QWidget
)

class Word(QObject):

    CurrentProgress = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.wordlist = ['p','y', 't', 'h', 'o', 'n']
        self.to_send_info = ['*', '*', '*', '*', '*', '*']
        self.guesses_counter = 9

    def check_letter(self, letter):
        self.guesses_counter = self.guesses_counter -1
        letter = letter.lower()
        if letter in self.wordlist:
            n = self.wordlist.index(letter)
            self.to_send_info[n] = letter
            self.CurrentProgress.emit(self.to_send_info)
        else:
            self.CurrentProgress.emit(self.to_send_info)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guess my word!")

        self.lab = QLabel("* * * * * *")
        self.lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.line = QLineEdit()

        self.btn = QPushButton("GUESS")

        self.glab = QLabel("U have 9 guesses left!")

        self.word = Word()
        self.word.CurrentProgress.connect(self.show_result)
        self.btn.clicked.connect(self.get_info)

        mainlay = QVBoxLayout()
        mainlay.addWidget(self.lab)
        mainlay.addWidget(self.line)
        mainlay.addWidget(self.btn)
        mainlay.addWidget(self.glab)

        cener = QWidget()
        cener.setLayout(mainlay)
        self.setCentralWidget(cener)

    def get_info(self):
        letter = self.line.text()
        self.word.check_letter(letter)

    def show_result(self, to_send_info):
        counter = self.word.guesses_counter
        if counter == 0:
            self.glab.setText("You run out of guesses!")
            self.line.clear()
            self.line.setReadOnly()
            self.lab.setText(" ".join(self.word.wordlist))
        else:
            result = " ".join(self.word.to_send_info)
            self.lab.setText(result)
        self.glab.setText(f"{counter} guesses left!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
