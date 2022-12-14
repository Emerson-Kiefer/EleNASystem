import os
import xml.etree.cElementTree as ET
import sys
import json
import urllib.request
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../Model')
sys.path.insert(0, DS_path)
from Node import Node

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

def elevation_post(req_data):
    API_ENDPOINT = "https://api.open-elevation.com/api/v1/lookup"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    r = requests.post(url = API_ENDPOINT, data = json.dumps(req_data), headers=headers)
    return r

def changeNodesElevation(dict_of_nodes, elevation_data):
    for res in elevation_data.get("results"):
        for node in dict_of_nodes.values():
            if (node.getLatitude() == res.get("latitude") and node.getLongitude() == res.get("longitude")):
                node.setElevation(float(res.get("elevation")))

def createNodesFromOSM(filepath):
    node_dict = dict()

    for event, elem in ET.iterparse(filepath, events=("start",)):

        if (elem.tag == "node"):
            temp = elem.attrib
            node_dict[temp.get("id")] = Node(int(temp.get("id")), float(temp.get("lat")), float(temp.get("lon")), 0.0)
    
    return node_dict

def addNodesNeighbors(node_dict):
    pass

def storeDictAsTxt(node_dict):
    pass

def loadDictFromTxt(filepath):
    pass
