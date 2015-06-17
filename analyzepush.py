f=open("push-log.txt", "r")

timeString = []
timeSecond = []

#transfer time string to seconds
def timeToSeconds(timeStr) :
	day=float(timeStr[8:10])
	hour=float(timeStr[11:13])
	minute=float(timeStr[14:16])
	second=float(timeStr[17:29])
	#print timeStr[8:10], timeStr[11:13], timeStr[14:16], timeStr[17:29]
	#print day, hour, minute, second
	return day*86400+hour*3600+minute*60+second;
	

# calculate the interval between the begin time and end time
def timeInterval(begin, end):
	day=float(begin[9:10])
	#hour=fload()
	return interval;



while True:
	line=f.readline()
	if line:
		# push begin
		# check whether image layers exist in the registry 
		if 'GET /v2/ HTTP/1.1' in line : 
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
	else:
		break

layerNumber=(len(timeString)-2)/5

print layerNumber

		
		
for k, v in enumerate(timeString):
	#print k, v
	timeSecond.append(timeToSeconds(timeString[k]))
	#print '%.9f' % timeToSeconds(timeString[k])

for k, v in enumerate(timeString):
	print '%.9f' % timeSecond[k]

	
#totalPushTime=timeInterval(timeString[0],timeString[len(timeString)-1])

#print totalPushTime
		
		
f.close()
		
