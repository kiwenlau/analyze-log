#!/bin/bash

imagelist=(axle-base sultans-bin haproxy cb-shell dnsutils node-metrics container-metrics ruby-base ipsec multilevel drupal jruby openjdk mono glassfish jenkins-slave quickstart-python exhibitor ubuntu-perl swagger-editor serf dnsmasq gocd-base gocd-agent drill ubuntu-perl-dev devmachine buildpack-runner gcc buildstep gocd-server)

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