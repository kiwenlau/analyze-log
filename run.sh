#!/bin/bash

imagelist=(axle-base gocd-server)

rm -rf output0 &> /dev/null
mkdir output0

for imagename in ${imagelist[*]};
do
    rm push-pull-log.txt push-logs.txt pull-logs.txt &> /dev/null
	  ./getpushpull.py logs/$imagename.txt
    ./separatepushpull.py
    ./calculatepush.py > output0/$imagename.txt
		#break
done

rm push-pull-log.txt push-logs.txt pull-logs.txt