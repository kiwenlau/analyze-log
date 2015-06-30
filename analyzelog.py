#!/usr/bin/python

# get all push and pull log
# write all push and pull log into "push-pull-log.txt"

f=open("axle-base.txt", "r")

line=f.readline()
while line :
    # the begin of push log or pull log
    if 'GET /v2/ HTTP/1.1' in line :
        fpushpull=open("push-pull-log.txt", "a");
        while line :
            fpushpull.write(line)
            # the end of push log or pull log
            if ('PUT /v1/repositories/' in line) and ('images' in line) or (line == "\n"):
                fpushpull.write("\n")
                break
            else :
                line=f.readline()
    line=f.readline()

f.close()
fpushpull.close()
