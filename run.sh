#!/bin/bash

loglist=(axle-base gocd-server)

rm -rf output &> /dev/null
mkdir output

for logname in ${loglist[*]};
do
    rm push-pull-log.txt push-logs.txt pull-logs.txt &> /dev/null
	  ./analyzelog.py logs/$logname.txt
    ./separatepushpull.py
    ./analyzepush.py > output/$logname.txt
		#break
done

rm push-pull-log.txt push-logs.txt pull-logs.txt