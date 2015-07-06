#!/usr/bin/python

# for each step of push, calculate the average time of 10 execution output
# omit the 2 largest and 2 smallest output

import sys
import numpy


# calculate the layer number 
# calculate the index of consecutive execution output
# read the whole files
f=open(sys.argv[1], "r")
line = f.readline().rstrip("\n")
layerNumber = int(line[16:])
index = 13+3*layerNumber
lines = f.readlines()
f.close()


totalTime = []
checkTime = []

# get all total push time and check time
for i in range(0, 9) :
    total=float(lines[i*index].rstrip("\n"))
    #print total
    totalTime.append(total)
    check=float(lines[i*index+1].rstrip("\n"))
    #print check
    checkTime.append(check)


# get the index of 2 largest total push time
max2=sorted(range(len(totalTime)), key=lambda i: totalTime[i])[-2:]

# get the index of 2 smallest total push time
min2=sorted(range(len(totalTime)), key=lambda i: totalTime[i])[:2]

#print totalTime
#print max2
#print min2

# trim is the index of omitted output
trim = max2 + min2


def averageTime (Time, trim) :
    for i in trim :
        Time[i] = 0
    #print Time
    return reduce(lambda x, y: x + y, Time) / (len(Time)- len(trim))

# calculate the average total time
averageTotalTime = averageTime(totalTime, trim)
print averageTotalTime

# calculate the average check time
averageCheckTime = averageTime(checkTime, trim)
print averageCheckTime


# calculate the average time for transforing the json file for each layers
jsonMatrix = numpy.zeros((6, layerNumber))

reserved = [x for x in range(10) if x not in trim ]
#print reserved

j=0
for i in reserved :
    jsonMatrix[j] = lines[(4+i*index) : (4+i*index+layerNumber)]
    #print jsonMatrix[j]
    j = j+1

#print "\n\n\n"

jsonMatrix2=numpy.transpose(jsonMatrix)
#print jsonMatrix2

averageJsonTime = []

for i in range(layerNumber) :
    averageJson = reduce(lambda x, y: x + y, jsonMatrix2[i]) / 6
    averageJsonTime.append(averageJson)


print "\njsontime:"
for x in averageJsonTime :
    print x


# calculate the average time for transforing json, layer and checksum of all layers
def averageLayerTime(offset) :
    timeMatrix = numpy.zeros((6, layerNumber))
    reserved = [ x for x in range(10) if x not in trim ]
    j = 0
    for i in reserved :
        timeMatrix[j] = lines[(offset + i*index) : (offset + i*index + layerNumber)]
        j = j + 1
    #print timeMatrix
    timeMatrix2 = numpy.transpose(timeMatrix) 
    averageTime = []
    for i in range(layerNumber) :
        average = reduce(lambda x, y : x + y, timeMatrix2[i]) / 6
        averageTime.append(average)
    print "\n"
    for x in averageTime:
        print x

averageLayerTime(4)
averageLayerTime(6+layerNumber)
averageLayerTime(8+layerNumber*2)       
    



























