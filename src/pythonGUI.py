import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
import pyqtlet_map_widget

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget

class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([42.38646066688732, -72.52584380181533], 10)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.marker = L.marker([42.38646066688732, -72.52584380181533])
        self.marker.bindPopup('Maps are a treasure.')
        self.map.addLayer(self.marker)
        self.show()



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        wid = MapWindow()
        
        self.setCentralWidget(wid)
            

        self.setMinimumSize(QSize(1000, 700))    
        self.setWindowTitle("520 EleNA Project") 

        self.start_label = QLabel(self)
        self.start_label.setText('Start Coordinates:')
        self.line = QLineEdit(self)

        self.line.move(120, 90)
        self.line.resize(100, 28)
        self.start_label.move(20, 90)
        self.start_label.setWordWrap(True)

        self.dest_label = QLabel(self)
        self.dest_label.setText("Destination Coordinates:")
        self.line2 = QLineEdit(self)
        self.dest_label.setWordWrap(True)

        self.line2.move(120, 150)
        self.line2.resize(100, 28)
        self.dest_label.move(20, 150)

        self.dist_label = QLabel(self)
        self.dist_label.setText("% of Optimal Distance:")
        self.line3 = QLineEdit(self)
        self.dist_label.setWordWrap(True)

        self.line3.move(120, 210)
        self.line3.resize(100, 28)
        self.dist_label.move(20, 210)

        pybutton = QPushButton('Go', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(20, 260) 

        
            

    def clickMethod(self):
        print('Your name: ' + self.line.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )