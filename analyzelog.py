#!/usr/bin/python

f=open("axle-base.txt", "r")

line=f.readline()
while line :
    if 'GET /v2/ HTTP/1.1' in line :
        fpush=open("push-log.txt", "a");
        while line :
            fpush.write(line)
            if ('PUT /v1/repositories/' in line) and ('images' in line) or (line == "\n"):
                fpush.write("\n")
                break
            else :
                line=f.readline()
    line=f.readline()

