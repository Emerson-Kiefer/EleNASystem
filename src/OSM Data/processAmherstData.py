from parseMap import *
import os

cur_path = os.path.dirname(__file__)
new_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")

# print(new_dic)

# Iterating over the nodes
for node in new_dic.values():
    # Checking if the current node has exactly 2 neighbors
    
    neighborDict = node.getNeighbors()
    
    if (len(neighborDict) == 2):

        # Checking if the neighbors also have exactly two neighbors
        flag = True
        for neighborNode in neighborDict.values():
            neighborsOfNeighbor  = neighborNode.get("neighbor").getNeighbors()
            if (len( neighborsOfNeighbor )) != 2:
                flag = False
                break

        if flag:
            print(node)
            print(neighborDict)
            print("____________^^ UNPROCESSED ^^____________")

            neighbor1 = None
            neighbor2 = None
            for neighborNode in neighborDict.values():
                temp = neighborNode.get("neighbor")
                if neighbor1 == None:
                    neighbor1 = temp
                elif neighbor2 == None:
                    neighbor2 = temp
            
            print(neighbor1)
            print(neighbor2)
            print("____________^^ NEIGHBORS ^^____________")

            neighbor1.removeNeighbor(node)
            neighbor2.removeNeighbor(node)

            neighbor1.addNeighbor(neighbor2)
            neighbor2.addNeighbor(neighbor1)

            print(node)
            print(neighborDict)
            print("____________^^ PROCESSED ^^____________")


# storeDictAsTxt(new_dic, cur_path + "/AbbrevAmherstNodesWNeighbors")
# abbrev_dic = loadDictFromTxt(cur_path + "/AbbrevAmherstNodesWNeighbors")