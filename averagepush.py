#!/usr/bin/python

import sys
import numpy


# cal
f=open(sys.argv[1], "r")
line = f.readline().rstrip("\n")
layerNumber = int(line[16:])
index = 13+3*layerNumber
lines = f.readlines()
f.close()



totalTime = []
checkTime = []

# get all total push time
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

trim = max2 + min2


def averageTime (Time, trim) :
    for i in trim :
        Time[i] = 0
    #print Time
    return reduce(lambda x, y: x + y, Time) / (len(Time)-4)

averageTotalTime = averageTime(totalTime, trim)
print averageTotalTime

averageCheckTime = averageTime(checkTime, trim)
print averageCheckTime

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





























