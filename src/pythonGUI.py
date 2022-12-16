import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget
import json
from Model import Node
#from Model import A_Star

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
        self.map.setView([29.66534, 72.64021], 10)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.marker = L.marker([42.38646066688732, -72.52584380181533])
        self.marker.bindPopup('Maps are a treasure.')
        self.map.addLayer(self.marker)
        self.map.setMaxBounds = [[-90, -180], [90, 180]]
        self.show()

        #Preventing the tiles from wrapping
        # wrapDic = {"noWrap": "true", "bounds": [ [-90, -180], [90, 180]]}
        # wrapJSON = json.dumps(wrapDic)
        
        # L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', wrapJSON).addTo(self.map)


         



class MainWindow(QMainWindow):
    wid = ''

    def __init__(self):
        QMainWindow.__init__(self)

        self.wid = MapWindow()
        
        self.setCentralWidget(self.wid)
            

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

    # def addRoutePath(self, list_nodes):
    #     latlngs = []
    #     for i in list_nodes:
    #         arr = []
    #         arr.append(i.getLatitude())
    #         arr.append(i.getLongitude())
    #         latlngs.append(arr)
    #     colorDic = {"color": "red"}
    #     colorJSON = json.dumps(colorDic)
    #     lineField = L.polyline(latlngs, colorJSON)
    #     lineField.addTo(self.wid.map)

    def temp(self):
        latlngs = [
            [42.407041496790995, -72.52918404268026],
            [42.38348334862606, -72.5202090419146],
            [42.36968346799125, -72.51892192908215],            
        ]
        colorDic = {"color": "red"}
        colorJSON = json.dumps(colorDic)
        lineField = L.polyline(latlngs,colorJSON).addTo(self.wid.map)

       

    # def searchPath(origin, destination):
    #     aStar_object = A_Star () 
    #     list_nodes = aStar_object.a_star(origin, destination)
    #     addRoutePath(list_nodes)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.temp()
    mainWin.show()
    sys.exit( app.exec_() )