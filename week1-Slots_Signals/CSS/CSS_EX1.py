import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Styled MainWindow")

# Створюємо центральний віджет
central_widget = QWidget()
central_widget.setStyleSheet("""
QWidget {
    background-color: #ecf0f1;   /* Світло-сірий фон */
    border: 3px solid #3498db;   /* Рамка */
    border-radius: 10px;         /* Заокруглені кути */
}
""")

window.setCentralWidget(central_widget)
window.resize(400, 300)
window.show()
sys.exit(app.exec())
