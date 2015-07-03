#!/usr/bin/python

f=open("push-logs.txt", "r")

#transfer time string to seconds
def timeToSeconds(timeStr) :
	day=float(timeStr[8:10])
	hour=float(timeStr[11:13])
	minute=float(timeStr[14:16])
	second=float(timeStr[17:29])
	return day*86400+hour*3600+minute*60+second;

def calculatePushTime(timeString = [], *args) :
    # transfer timestamp to second
    timeSecond = []
    for k, v in enumerate(timeString):
        timeSecond.append(timeToSeconds(timeString[k]))
    layerNumber=(len(timeString)-2)/5
    print "layer number : " , layerNumber
    totalPushTime = timeSecond[len(timeString)-1]-timeSecond[0]
    print totalPushTime
    checkTime = timeSecond[2*layerNumber] - timeSecond[0]
    print checkTime
    
    i=2*layerNumber+1
    jsonTime = []
    layerTime = []
    checksumTime = []
    while i<len(timeString)-3:
        jsonTime.append(timeSecond[i+1]-timeSecond[i])
        layerTime.append(timeSecond[i+2]-timeSecond[i+1])
        checksumTime.append(timeSecond[i+3]-timeSecond[i+2])
        i = i + 3
    print "\njsonTime"
    for k, v in enumerate(jsonTime) :
        print v
    print "\nlayerTime"
    for k, v in enumerate(layerTime) :
        print v
    print "\nchecksumTime"
    for k, v in enumerate(checksumTime) :
        print v
    print "\n\n\n"
    return

timeString = []

line=f.readline()
while line :
    while line != "\n" :
        # push begin
        # check whether image layers exist in the registry
        if "GET /v2/ HTTP/1.1" in line :
            timeString.append(line[:29])
        # finish the check
        if (('GET /v1/images/' in line) and ('/json' in line)) :
            timeString.append(line[:29])
        # push image layers
        if (('args =' in line) and ('image_id' in line)) :
            timeString.append(line[:29])
        # push finish
        if (('PUT /v1/repositories/' in line) and ('images' in line)) :
            timeString.append(line[:29])
        line=f.readline()
    calculatePushTime(timeString)
    timeString = []
    line=f.readline()
#break

f.close()
		
