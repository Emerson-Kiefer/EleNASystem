import os
import xml.etree.cElementTree as ET
import sys
import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# from srtm import Srtm1HeightMapCollection
# import pyrosm

cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../Model')
sys.path.insert(0, DS_path)
from Node import Node

# fp = pyrosm.get_data("massachusetts", directory=cur_path)
# osm = pyrosm.OSM(fp)
# # print(osm.filepath)
# nodes,edges = osm.get_network(network_type="driving",nodes=True)

# print(nodes)


osm_file = cur_path+"/map.osm"

# tree = ET. parse(osm_file)
# root = tree.getroot()
# print(" Print root Information")
# print(root)

# dictionary mapping string id to a Node object
node_dict = dict()
# srtm1_data = Srtm1HeightMapCollection()

def elevation(lat, lng):
    url = 'https://api.open-elevation.com/api/v1/lookup?'
   #  print(url+"locations="+str(lat)+","+str(lng))
    request = urllib.request.urlopen(url+"locations="+str(lat)+","+str(lng))
    
    try:
        results = json.load(request).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            # ELEVATION
            return elevation
        else:
            print('HTTP GET Request failed.')
    except:
        print('JSON decode failed: '+str(request))

i = 0
for event, elem in ET.iterparse(osm_file, events=("start",)):
   if (elem.tag == "node"):
      temp = elem.attrib
      elev = elevation(temp.get("lat"), temp.get("lon"))
      node_dict[temp.get("id")] = Node(int(temp.get("id")), float(temp.get("lat")), float(temp.get("lon")), float(elev))
      print(elev)
      # print(node_dict)
   i += 1
   if i == 100:
      break

print(node_dict)
with open('parsedData.txt', 'w') as convert_file:
     convert_file.write(json.dumps(node_dict))
