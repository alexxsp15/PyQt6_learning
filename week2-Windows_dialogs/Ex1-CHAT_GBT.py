import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QDialog, QLabel, QVBoxLayout, QMessageBox
)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Це діалог")

        self.label = QLabel("Привіт! Це діалогове вікно.")
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Головне вікно")

        self.button = QPushButton("Відкрити діалог")
        self.button.clicked.connect(self.show_dialog)

        self.setCentralWidget(self.button)

    def show_dialog(self):
        dialog = MyDialog()
        result = dialog.exec()

        if result:
            # ✅ Показуємо повідомлення
            QMessageBox.information(
                self,
                "Результат",
                "Ви натиснули OK у діалозі!"
            )
        else:
            QMessageBox.warning(
                self,
                "Закрито",
                "Діалог було закрито або скасовано."
            )

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
