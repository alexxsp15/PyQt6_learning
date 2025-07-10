import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMenu, QToolBar,
    QDockWidget, QListWidget
)
from PyQt6.QtGui import QIcon, QAction, QKeySequence
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window Example")
        self.resize(800, 600)

        # Дії
        new_act = QAction(QIcon.fromTheme("document-new"), "&New", self)
        new_act.setShortcut("Ctrl+N")
        new_act.setStatusTip("Create a new file")
        new_act.triggered.connect(self.new_file)

        open_act = QAction(QIcon.fromTheme("document-open"), "&Open...", self)
        open_act.setShortcut("Ctrl+O")
        open_act.setStatusTip("Open an existing file")
        open_act.triggered.connect(self.open_file)

        # Меню
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_act)
        file_menu.addAction(open_act)
        file_menu.addSeparator()

        # Тулбар
        file_toolbar = self.addToolBar("File")
        file_toolbar.addAction(new_act)
        file_toolbar.addAction(open_act)
        file_toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, file_toolbar)

        # Док-віджет
        dock = QDockWidget("Table of Contents", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)

        heading_list = QListWidget()
        heading_list.addItems(["Introduction", "Chapter 1", "Chapter 2"])
        dock.setWidget(heading_list)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        # Розміщення доків по кутах
        self.setCorner(Qt.Corner.TopLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)
        self.setCorner(Qt.Corner.BottomLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)
        self.setCorner(Qt.Corner.TopRightCorner, Qt.DockWidgetArea.RightDockWidgetArea)
        self.setCorner(Qt.Corner.BottomRightCorner, Qt.DockWidgetArea.RightDockWidgetArea)

    def new_file(self):
        print("New file action triggered")

    def open_file(self):
        print("Open file action triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
