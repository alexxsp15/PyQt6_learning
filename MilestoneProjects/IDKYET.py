import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget, QLabel, QSlider, QCheckBox, QLineEdit, \
    QVBoxLayout, QPushButton


class MyDock(QDockWidget):
    Text = pyqtSignal(str)
    Size = pyqtSignal(int)
    FontColor = pyqtSignal(int, int, int)
    def __init__(self):
        super().__init__()

        dockWidget = QWidget()
        dockLay = QVBoxLayout()

        self.TextLine = QLineEdit()

        self.SizeChanger = QSlider()
        self.SizeChanger.setOrientation(Qt.Orientation.Horizontal)
        self.SizeChanger.setRange(0, 70)

        self.redSlider = QSlider()
        self.redSlider.setOrientation(Qt.Orientation.Horizontal)
        self.redSlider.setRange(0, 255)
        self.greenSlider = QSlider()
        self.greenSlider.setOrientation(Qt.Orientation.Horizontal)
        self.greenSlider.setRange(0, 255)
        self.blueSlider = QSlider()
        self.blueSlider.setOrientation(Qt.Orientation.Horizontal)
        self.blueSlider.setRange(0, 255)

        self.confirmButton = QPushButton("Confirm")


        self.confirmButton.clicked.connect(self.get_text)
        self.SizeChanger.valueChanged.connect(self.get_size)
        self.redSlider.valueChanged.connect(self.get_font_color)
        self.greenSlider.valueChanged.connect(self.get_font_color)
        self.blueSlider.valueChanged.connect(self.get_font_color)

        dockLay.addWidget(self.TextLine)
        dockLay.addWidget(self.SizeChanger)
        dockLay.addWidget(self.redSlider)
        dockLay.addWidget(self.greenSlider)
        dockLay.addWidget(self.blueSlider)
        dockLay.addWidget(self.confirmButton)

        dockWidget.setLayout(dockLay)
        self.setWidget(dockWidget)

    def get_text(self):
        text = self.TextLine.text()
        self.Text.emit(text)

    def get_size(self):
        s = self.SizeChanger.value()
        self.Size.emit(s)

    def get_font_color(self):
        r = self.redSlider.value()
        g = self.greenSlider.value()
        b = self.blueSlider.value()
        self.FontColor.emit(r, g, b)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainWidget = QWidget()
        mainWidget.setFixedSize(800, 600)
        mainLay = QVBoxLayout()

        self.color = ()
        self.backgroundColor = ()
        self.border = 0
        self.borderRadius = 0
        self.padding = 0
        self.font_Size = 60
        self.font_weight = ""

        self.MainLabel = QLabel("@ <-ur nickname then")
        self.MainLabel.setStyleSheet(f"font-size: {self.font_Size}px;")

        self.dok = MyDock()
        self.dok.Text.connect(self.show_text)
        self.dok.Size.connect(self.show_size)
        self.dok.FontColor.connect(self.show_color)

        mainLay.addWidget(self.MainLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        mainWidget.setLayout(mainLay)
        self.setCentralWidget(mainWidget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dok)

    def show_text(self, txt):
        self.MainLabel.setText(f"@{txt}")

    def show_size(self, s):
        self.font_Size = s
        self.MainLabel.setStyleSheet(f"""
                QLabel {{
                    color: {self.color};                                         
                    background-color: {self.backgroundColor};                  
                    border: {self.border}px;                   
                    border-radius: {self.borderRadius}px;                               
                    padding: {self.padding}px;                                           
                    font-size: {self.font_Size}px;                                        
                    font-weight: {self.font_weight}; 
                }}""")

    def show_color(self, r, g, b):
        self.color = f"rgb({r}, {g}, {b})"
        self.MainLabel.setStyleSheet(f"""
        QLabel {{
            color: {self.color};
            background-color: {self.backgroundColor};                  
            border: {self.border}px;
            border-radius: {self.borderRadius}px;
            padding: {self.padding}px;
            font-size: {self.font_Size}px;
            font-weight: {self.font_weight};
        }}""")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()