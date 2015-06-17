f=open("axle-base.txt", "r")

while True:
	line=f.readline()
	if line:
	    if 'GET /v2/ HTTP/1.1' in line :
		    print line
	else:
		break
		
