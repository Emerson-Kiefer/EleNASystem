import os
import xml.etree.cElementTree as ET
import sys
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

for event, elem in ET.iterparse(osm_file, events=("start",)):
   if (elem.tag == "node"):
      temp = elem.attrib
      node_dict[temp.get("id")] = Node(int(temp.get("id")), float(temp.get("lat")), float(temp.get("lon")), 0.0)

print(node_dict)