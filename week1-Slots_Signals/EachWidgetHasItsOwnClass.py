import random

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import sys

class CounterButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                color: black;
                border: 2px solid gray;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: lightgreen;
            }
        """)

        self.n1 = 0
        self.n2 = 0

    def mousePressEvent(self, e):
        self.n1 = self.n1 +1
        print(f"Pressed {self.n1}th time")
        super().mousePressEvent(e)


    def mouseReleaseEvent(self, e):
        self.n2 = self.n2 + 1
        print(f"c ya {self.n2}!")
        super().mouseReleaseEvent(e)

class ChangesColor(QPushButton):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;      
                color: #ecf0f1;                  
                border: none;
                border-radius: 12px;           
                padding: 10px 20px;             
                font-size: 16px;
                font-weight: bold;
                letter-spacing: 1px;
                transition: all 0.3s;
            }
            QPushButton:hover {
                background-color: #34495e;      
                color: #1abc9c;                   
                box-shadow: 0 0 10px #1abc9c;     
            }
            QPushButton:pressed {
                background-color: #1abc9c;      
                color: #2c3e50;                  
            }
        """)

        self.color_list = [
            "white", "black", "red", "green", "blue", "yellow", "cyan", "magenta",
            "gray", "darkRed", "darkGreen", "darkBlue", "darkCyan", "darkMagenta", "darkYellow", "darkGray",
            "lightGray", "transparent", "aqua", "azure", "beige", "bisque", "brown", "chocolate", "coral",
            "crimson", "fuchsia", "gainsboro", "gold", "goldenrod", "hotpink", "indianred", "indigo", "ivory",
            "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral",
            "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightpink", "lightsalmon", "lightseagreen",
            "lightskyblue", "lightslategray", "lightsteelblue", "lime", "limegreen", "linen", "maroon",
            "mediumaquamarine",
            "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
            "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite",
            "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen",
            "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue",
            "purple", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell",
            "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan",
            "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "whitesmoke", "yellowgreen"
        ]
        self.color = 0
    def wheelEvent(self, a0):
        self.color = random.choice(self.color_list)
        self.setStyleSheet(f"background-color: {self.color};")
        super().wheelEvent(a0)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")

        lay = QVBoxLayout()

        self.btn = CounterButton()
        self.btn1 = ChangesColor()

        lay.addWidget(self.btn)
        lay.addWidget(self.btn1)
        self.setLayout(lay)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
