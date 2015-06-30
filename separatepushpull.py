#!/usr/bin/python

# separate push and pull log

f=open("push-pull-log.txt", "r")

line=f.readline()
while line :
    # push log
    fpush=open("push-logs.txt", "a")
    while line != "\n" :
        fpush.write(line)
        line=f.readline()
    fpush.write(line)
    line=f.readline()
    # pull log
    fpull=open("pull-logs.txt", "a")
    while line != "\n" :
        fpull.write(line)
        line=f.readline()
    fpull.write(line)
    line=f.readline()
    line=f.readline()

f.close()
fpush.close()
fpull.close()