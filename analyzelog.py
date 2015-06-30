#!/usr/bin/python

f=open("axle-base.txt", "r")

# for push i%2==0; for pull i%2==1
i=0

# get the push log from the original log
while True:
	line=f.readline()
	if line:
		if 'GET /v2/ HTTP/1.1' in line :
			if i%2==0 :
				fpush=open('push-log.txt', 'w')
				fpush.write(line)
				line=f.readline()
				while not (('PUT /v1/repositories/' in line) and ('images' in line)) :
					line=f.readline()
					fpush.write(line)
				fpush.close()
				break
				print 'push'
			else :
				print 'pull'
			i+=1
	else:
		break

f.close()
		
