import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel 

# Initialize the pyqt5 application
if __name__ == '__main__':
    a = QApplication(sys.argv)

# Let's set the size, title, width, etc.
form = QWidget()
form.resize(200, 100)
form.move(300, 300)
form.setWindowTitle('Mini GUI for Avenchurin')

label = QLabel('Avenchurin is very hot')
label.move(50, 40)
label.setParent(form)

form.show() # Show the GUI

a.exec_() # Execute the GUI
