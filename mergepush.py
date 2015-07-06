#!/usr/bin/python

import os
import shutil


files = os.listdir("output1")


totalTime = []
checkTime = []
jsonTime = []
layerTime = []
checksumTime = []

for file in files :
    f = open("output1/"+file)
    line = f.readline().rstrip("\n")
    layerNumber = int(line[16:])
    lines = f.readlines()
    totalTime.append(lines[0])
    checkTime.append(lines[1])
    jsonTime = jsonTime + lines[ 4 : ( 4 + layerNumber ) ]
    layerTime = layerTime + lines[ ( 6 + layerNumber ) : ( 6 + layerNumber*2 ) ]
    checkTime = checkTime + lines[ ( 8 + layerNumber*2 ) : ( 8 + layerNumber*3 ) ]
    f.close()
    
def writeListToFile(listname, filename) :
    f = open(filename, "w")
    for x in listname :
        f.write(x.rstrip("/n"))
    f.close()
    return

if os.path.exists("output2"):
    shutil.rmtree("output2")

os.mkdir("output2")

writeListToFile(totalTime, "output2/totalTime.txt")
        
    
        




























