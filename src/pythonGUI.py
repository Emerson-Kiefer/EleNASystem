import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
import pyqtlet_map_widget

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1000, 700))    
        self.setWindowTitle("520 EleNA Project") 

        self.start_label = QLabel(self)
        self.start_label.setText('Start Coordinates:')
        self.line = QLineEdit(self)

        self.line.move(120, 20)
        self.line.resize(200, 32)
        self.start_label.move(20, 20)
        self.start_label.setWordWrap(True)

        self.dest_label = QLabel(self)
        self.dest_label.setText("Destination Coordinates:")
        self.line2 = QLineEdit(self)
        self.dest_label.setWordWrap(True)

        self.line2.move(120, 80)
        self.line2.resize(200, 32)
        self.dest_label.move(20, 80)

        self.dist_label = QLabel(self)
        self.dist_label.setText("% of Optimal Distance:")
        self.line3 = QLineEdit(self)
        self.dist_label.setWordWrap(True)

        self.line3.move(120, 140)
        self.line3.resize(200, 32)
        self.dist_label.move(20, 140)

        pybutton = QPushButton('Go', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(20, 200)        

    def clickMethod(self):
        print('Your name: ' + self.line.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )