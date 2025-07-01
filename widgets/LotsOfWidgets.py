import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            #cheack box
            QCheckBox,

            #dropdown list
            QComboBox,

            #edit date
            QDateEdit,

            #edit date + time
            QDateTimeEdit,

            #sircle-controller
            QDial,

            #pole with float num
            QDoubleSpinBox,

            #dropdown with fronts
            QFontComboBox,

            #
            QLCDNumber,

            #label
            QLabel,

            #text pole
            QLineEdit,

            #progress(%)
            QProgressBar,

            #button
            QPushButton,

            #choose 1 from a group of objects
            QRadioButton,

            #slider
            QSlider,

            #pole with integers and buttons + / -
            QSpinBox,

            #pole with time editing
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()