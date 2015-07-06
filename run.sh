#!/bin/bash

imagelist=(axle-base gocd-server)

rm -rf output0 output1&> /dev/null
mkdir output0 output1

for imagename in ${imagelist[*]};
do
    rm push-pull-log.txt push-logs.txt pull-logs.txt &> /dev/null
	  ./getpushpull.py logs/$imagename.txt
    ./separatepushpull.py
    ./calculatepush.py > output0/$imagename.txt
		#break
done

rm push-pull-log.txt push-logs.txt pull-logs.txt

for imagename in ${imagelist[*]};
do
    ./averagepush.py output0/$imagename.txt > output1/$imagename.txt
#break
done