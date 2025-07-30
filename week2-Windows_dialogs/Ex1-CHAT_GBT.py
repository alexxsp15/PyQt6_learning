import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTabWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget приклад")
        self.setGeometry(100, 100, 500, 400)

        # Створюємо QTabWidget
        self.tabs = QTabWidget()

        # Вкладка 1
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.tab1_layout.addWidget(QLabel("Це вкладка 1"))
        self.tab1.setLayout(self.tab1_layout)
        self.tabs.addTab(self.tab1, "Головна")

        # Вкладка 2
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.tab2_layout.addWidget(QLabel("Це вкладка 2"))
        self.tab2.setLayout(self.tab2_layout)
        self.tabs.addTab(self.tab2, "Налаштування")

        # Вкладка 3
        self.tab3 = QWidget()
        self.tab3_layout = QVBoxLayout()
        self.tab3_layout.addWidget(QLabel("Це вкладка 3"))
        self.tab3.setLayout(self.tab3_layout)
        self.tabs.addTab(self.tab3, "Про програму")

        # Встановлюємо вкладки як центральний віджет
        self.setCentralWidget(self.tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
