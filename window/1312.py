from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QDockWidget,
    QTextEdit, QMainWindow, QApplication
)
from PyQt6.QtCore import Qt

app = QApplication([])

main = QMainWindow()

dock = QDockWidget()
dock.setWidget(QTextEdit("Контент дока"))

# ⚙️ Особливості: закривається, рухається тощо
dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable)

# 🔧 Кастомний заголовок
title_bar = QWidget()
layout = QHBoxLayout(title_bar)
layout.setContentsMargins(5, 2, 5, 2)

label = QLabel("📁 Панель")
close_btn = QPushButton("❌")
close_btn.setFixedSize(25, 25)

layout.addWidget(label)
layout.addStretch()
layout.addWidget(close_btn)

dock.setTitleBarWidget(title_bar)

# 🔒 Закриття при натисканні
close_btn.clicked.connect(lambda: dock.setVisible(False))

main.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
main.resize(600, 400)
main.show()
app.exec()
