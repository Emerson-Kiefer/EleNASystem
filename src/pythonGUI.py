import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget
import json
from Model import Node
from GUISearchHelper import searchPath
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
        #self.marker = L.marker([42.38646066688732, -72.52584380181533])
        # self.marker = L.marker()
        # self.marker.bindPopup('Maps are a treasure.')
        # self.map.addLayer(self.marker)
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
            
        self.maxormin = ""

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

        self.slider = QtWidgets.QSlider(self)
        self.slider.valueChanged.connect(self.ElevationGain)
        self.slider.setGeometry(QtCore.QRect(200, 100, 160, 16))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.move(20, 250)

        self.radioButtonMax = QtWidgets.QRadioButton(self)
        self.radioButtonMax.setGeometry(QtCore.QRect(180, 120, 95, 20))
        self.radioButtonMax.toggled.connect(self.maxselected)
        self.radioButtonMax.setText("Max")
        self.radioButtonMax.move(225, 230)

        self.radioButtonMin = QtWidgets.QRadioButton(self)
        self.radioButtonMin.setGeometry(QtCore.QRect(180, 120, 95, 20))
        self.radioButtonMin.toggled.connect(self.minselected)
        self.radioButtonMin.setText("Min")
        self.radioButtonMin.move(225, 210)

        pybutton = QPushButton('Go', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(20, 270) 

    def maxselected(self, selected):
        if selected:
            self.maxormin = "maximize"
         

    def minselected(self, selected):
        if selected:
            self.maxormin = "minimize"   
            
    def ElevationGain(self,value):
        gain = 100
        self.line3.setText(str(gain))
        self.line3.setText(str(gain+(value//2)))


    def clickMethod(self):
        #Retrieves values from the textfields
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        origin = self.line.text()
        destination = self.line2.text()
        pdistance = self.line3.text()
        optdistance = self.maxormin

        if( origin == "" or destination == "" or pdistance == ""):
            msg_box.setText("You forgot to enter origin or destination or Optimal Distance")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

        elif("," not in origin or "," not in destination):
            msg_box.setText("Input format incorrect")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

        elif(optdistance == ""):
            msg_box.setText("Select Max or Min")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

        else:
            forigin_lat = float(origin.split(",")[0])
            forigin_lng = float(origin.split(",")[1])

            fdestination_lat = float(destination.split(",")[0])
            fdestination_lng = float(destination.split(",")[1])

            fpdistance = float (pdistance)

            if(forigin_lat > 90 or forigin_lat < -90 or fdestination_lat > 90 or fdestination_lat < -90 ):
                msg_box.setText("Incorrect Input. Change input and try again")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            
            elif(fdestination_lng > 180 or fdestination_lng < -180 or forigin_lng > 180 or forigin_lng < -180):
                msg_box.setText("Incorrect Input. Change input and try again")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            elif(fpdistance > 150 or fpdistance < 100):
                msg_box.setText("Optimal distance should be between 100 to 150")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            #Need to finish the function by calling a_star and addroutePath
            else:
                lat_long_orig = str(forigin_lat) + "," + str(forigin_lng)
                lat_long_dest = str(fdestination_lat) + "," + str(fdestination_lng)
                path_list = searchPath(lat_long_orig, lat_long_dest, fpdistance, optdistance)
                self.addRoutePath(path_list)



    def addRoutePath(self, list_nodes):
        latlngs = []
        #retrieve the list of coordinates
        for i in list_nodes:
            arr = []
            arr.append(i.getLatitude())
            arr.append(i.getLongitude())
            latlngs.append(arr)

        #draw line to represent the shortest path 
        colorDic = {"color": "red"}
        colorJSON = json.dumps(colorDic)
        lineField = L.polyline(latlngs, colorJSON)
        lineField.addTo(self.wid.map)

        #Set map view to show origin
        self.wid.map.setView(latlngs[0], 10)

        #Set markers on origin and destination
        self.wid.marker = L.marker(latlngs[0])
        self.wid.marker.addTo(self.wid.map)
        self.wid.marker = L.marker(latlngs[-1])
        self.wid.marker.addTo(self.wid.map)


    #Function to test addRoutePath
    def temp(self):
        # self.addRoutePath(searchPath("42.3726975,-72.5211276", "42.3734759,-72.521207", 100, "maximize"))
        # self.addRoutePath(searchPath("42.384805,-72.548099", "42.3841768,-72.5359462", 100, "maximize"))
        # self.addRoutePath(searchPath("42.354631,-72.587133", "42.3586812,-72.5785193", 100, "maximize"))
        self.addRoutePath(searchPath("42.354631,-72.587133", "42.373211,-72.545944", 100, "maximize"))
        
        # latlngs = [
        #     [42.407041496790995, -72.52918404268026],
        #     [42.38348334862606, -72.5202090419146],
        #     [42.36968346799125, -72.51892192908215],            
        # ]
        # colorDic = {"color": "red"}
        # colorJSON = json.dumps(colorDic)
        # lineField = L.polyline(latlngs,colorJSON).addTo(self.wid.map)
        # self.wid.map.setView(latlngs[0], 10)
        # self.wid.marker = L.marker(latlngs[0])
        # self.wid.marker.addTo(self.wid.map)
        # self.wid.marker = L.marker(latlngs[-1])
        # self.wid.marker.addTo(self.wid.map)




       

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