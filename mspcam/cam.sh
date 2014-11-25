#!/bin/bash

# Print the IP address
#_IP=$(hostname -I) || true
#if [ "$_IP" ]; then
#  printf "My IP address is %s\n" "$_IP"
#fi


filename=$(perl -e "print time")
foldername=$(date --rfc-3339=date)

#printf "$foldername"

curl http://localhost:8080/?action=snapshot > $filename
timestamp=`stat -c %y $filename`

if [ -f /mnt/dav/out/$foldername ]; then
  mkdir /mnt/dav/out/$foldername
fi

convert $filename -fill black -fill white -pointsize 15 -draw  "text 5,15 '${timestamp:0:19}'" /mnt/dav/out/$foldername/$filename.jpg

rm $filename

