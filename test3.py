f=open("axle-base.txt", "r")

# for push i%2==0; for pull i%2==1
i=0

while True:
	line=f.readline()
	if line:
	    if 'GET /v2/ HTTP/1.1' in line :
			if i%2==0 :
				print 'push'
			else :
				print 'pull'
			i+=1
	else:
		break
		
