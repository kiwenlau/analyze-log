#!/bin/bash

loglist=(axle-base.txt gocd-server.txt)

for logname in ${loglist[*]};
do
    rm push-pull-log.txt push-logs.txt pull-logs.txt &> /dev/null
	./analyzelog.py logs/$logname
    ./separatepushpull.py
    ./analyzepush.py
done

#rm push-pull-log.txt push-logs.txt pull-logs.txt