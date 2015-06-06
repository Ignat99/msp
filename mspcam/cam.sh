#!/bin/bash

# Print the IP address
#_IP=$(hostname -I) || true
#if [ "$_IP" ]; then
#  printf "My IP address is %s\n" "$_IP"
#fi


filename=$(perl -e "print time")
foldername=$(date --rfc-3339=date)
port=8080
portfilename=$port$filename

#printf "$foldername"

curl -u artak:123 http://localhost:$port/?action=snapshot > /tmp/$portfilename
timestamp=`stat -c %y /tmp/$portfilename`

if [ ! -f /mnt/dav/out/$foldername ]; then
  mkdir /mnt/dav/out/$foldername
fi

if [ ! -f /mnt/dav/out/$foldername/$port ]; then
  mkdir /mnt/dav/out/$foldername/$port
fi

convert /tmp/$portfilename -fill black -fill white -pointsize 15 -draw  "text 5,15 '${timestamp:0:19}'" /mnt/dav/out/$foldername/$port/$filename.jpg

rm /tmp/$portfilename

sudo arecord -B --buffer-time=1000000 -f dat -r 8000 -d 60 -D plughw:1,0 /mnt/dav/out/$foldername/$port/$filename.wav
sudo flac -f -s /mnt/dav/out/$foldername/$port/$filename.wav -o /mnt/dav/out/$foldername/$port/$filename.flac
