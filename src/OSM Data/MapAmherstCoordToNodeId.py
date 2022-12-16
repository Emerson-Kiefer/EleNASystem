from parseMap import *
import os

cur_path = os.path.dirname(__file__)
new_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")

lat_long_node_id = dict()

for key in new_dic:
    lat_long = ""
    node = new_dic.get(key)
    lat_long += (str(node.getLatitude()) + ",")
    lat_long += str(node.getLongitude())
    lat_long_node_id[lat_long] = key

# print(lat_long_node_id)
storeDictAsTxt(lat_long_node_id, cur_path + "/CoordinatesToNodeId")