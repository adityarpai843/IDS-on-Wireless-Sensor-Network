#!/bin/bash
type=rnd25-normal
total=200
delay=5
date=_$(date +%F_%H:%M)_
logfile=$type$date
declare -a nodes=(
"aaaa::212:7402:2:202" 
"aaaa::212:7403:3:303"
"aaaa::212:7404:4:404" 
"aaaa::212:7405:5:505" 
"aaaa::212:7406:6:606" 
"aaaa::212:7407:7:707"
"aaaa::212:7408:8:808" 
"aaaa::212:7409:9:909" 
"aaaa::212:740a:a:a0a" 
"aaaa::212:740b:b:b0b"
"aaaa::212:740c:c:c0c" 
"aaaa::212:740d:d:d0d" 
"aaaa::212:740e:e:e0e"
"aaaa::212:740f:f:f0f"
"aaaa::212:7410:10:1010" 
"aaaa::212:7411:11:1111" 
"aaaa::212:7412:12:1212" 
"aaaa::212:7413:13:1313"
"aaaa::212:7414:14:1414" 
"aaaa::212:7415:15:1515" 
"aaaa::212:7416:16:1616" 
"aaaa::212:7417:17:1717" 
"aaaa::212:7418:18:1818" 
"aaaa::212:7419:19:1919" 
"aaaa::212:741a:1a:1a1a"
		
		
)
dir="./traces/$type"
mkdir $dir
echo "creating case $type"
for i in "${nodes[@]}"
  do
    echo "Ping $i"
    
    
    log="$dir/$logfile$i.log"
    resp=`ping6 -c $total -i $delay $i > $log &`
    echo $resp
    sleep 1
  done

log="$dir/$logfile""routes.log"
resp=`lynx -dump http://[aaaa::212:7401:1:101] > $log &`
echo $resp
msg="I'm done"
#echo $msg

