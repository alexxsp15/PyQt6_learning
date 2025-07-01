from PyQt6.QtWidgets import QApplication, QWidget
import sys

#Create the main application object (required for any Qt app)
app = QApplication(sys.argv) #Python list containing the command line arguments passed to the application.


window = QWidget()
window.show()

#Start the event loop (keeps the application running and responsive)
app.exec()
