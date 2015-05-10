#!/bin/bash

filename=$(date --rfc-3339=date)
port=8080

i=0
for f in `ls -tr /mnt/dav/out/$filename/$port/*.jpg 2>/dev/null`
do
  newf=`printf %06d $i`.jpg
  echo $f "-->" $newf
  mv $f $newf
  i=$((i+1))
done
rmdir /mnt/dav/out/$filename/$port/
avconv -r 10 -i %06d.jpg -r 10 -vcodec mjpeg -qscale 1   /mnt/dav/$port$filename.avi
rm *.jpg

