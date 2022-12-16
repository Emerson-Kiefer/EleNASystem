import os
import sys
from SearchGraph import SearchGraph

cur_path = os.path.dirname(__file__)
parseMap_path = os.path.join(cur_path, '../OSM Data')
print(parseMap_path)
sys.path.insert(0, parseMap_path)

from parseMap import *

node_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")
coord_dic = loadDictFromTxt(cur_path + "/CoordinatesToNodeId")

# print(node_dic)
# print(coord_dic)

sg = SearchGraph(node_dic.get("10061124349"), node_dic.get("10061124350"), 100.0, "minimize")
sg.generatePaths()
# print(node_dic.get("10061124349"), node_dic.get("10061124350"))

# print(sg.getStartNode())
# print(sg.getGoalNode())
# print(sg._is_valid_mode(sg.getMode()))
print(sg.getShortestPath())
print(sg.getElevationPath())
print("\n")

sg = SearchGraph(node_dic.get("6302552898"), node_dic.get("10061124350"), 150.0, "maximize")
sg.generatePaths()
# print(node_dic.get("10061124349"), node_dic.get("10061124350"))

# print(sg.getStartNode())
# print(sg.getGoalNode())
# print(sg._is_valid_mode(sg.getMode()))
print(sg.getShortestPath())
print(sg.getElevationPath())