import os
import sys

cur_path = os.path.dirname(__file__)
parseMap_path = os.path.join(cur_path, './OSM Data')
searchGraph_path = os.path.join(cur_path, './Model')

sys.path.insert(0, parseMap_path)
sys.path.insert(0, searchGraph_path)

from SearchGraph import SearchGraph
from parseMap import *

def searchPath(lat_long_orig, lat_long_dest, percent_shortest_path, mode):
    node_dic = loadDictFromTxt(cur_path + "/AbbrevAmherstNodesWNeighbors")
    coord_dic = loadDictFromTxt(cur_path + "/CoordinatesToNodeId")

    originNodeId = coord_dic.get(lat_long_orig)
    destNodeId = coord_dic.get(lat_long_dest)
    # for key, val in coord_dic.items():
    #     if "10061124350" == val:
    #         print(key)
    # print(node_dic.get("10061124350"))
    # print(lat_long_dest in coord_dic)
    # print(originNodeId, destNodeId)

    originNode = node_dic.get(originNodeId)
    destNode = node_dic.get(destNodeId)

    sg = SearchGraph(originNode, destNode, float(percent_shortest_path), mode)
    sg.generatePaths()
    elev_path = sg.getElevationPath()

    list_of_nodes = []

    if not elev_path.get("validPath"):
        return list_of_nodes

    for p in elev_path.get("path"):
        list_of_nodes.append(node_dic.get(str(p)))
    
    return list_of_nodes

# print(searchPath("42.3726975,-72.5211276", "42.3734759,-72.521207", 100, "maximize"))

# print(searchPath("42.3734686,-72.5212206", "42.383278,-72.5183608", 100, "minimize"))
