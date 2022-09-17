#!/bin/bash
c=30
d=20

#memakai let
let jumlah=$c+$d
let kurang=$c-$d

#memakai expr
bagi=`expr $c / $d`
#memakai perintah subtitusi $((ekspresi))
mod=$(($c % $d))
echo "c + d = $jumlah"
echo "c - d = $kurang"

d=$c

p=50
m=10

if [ $p == $m ]
then
echo "c & d sama wae"
elif [ $p -gt $m ]
then
echo "c lebih GEDE dari d"
elif [ $p -lt $m ]
then
echo "d lebih cilik dari c"
else
echo "pasti error"
fi
