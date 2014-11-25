sudo apt-get install tightvncserver

vncserver :1 -geometry 1200x700 -depth 16

sudo dpkg-reconfigure tzdata

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install imagemagick

sudo apt-get install libav-tools

sudo apt-get install libjpeg8-dev

sudo apt-get install subversion

sudo svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer/ mjpg-streamer
cd mjpg-streamer
make

cd ..

sudo apt-get install davfs2
sudo mkdir /mnt/dav
sudo mount -t davfs https://webdav.yandex.ru /mnt/dav -o uid=pi,gid=pi

================================================

cd mjpg-streamer 
./mjpg_streamer -i "./input_uvc.so -r 1280x720 -f 1" -o "./output_file.so -f ./ -d 60000"

filename="2013_10_04_12_11_30_picture_000000000.jpg"
timestamp=`stat -c %y $filename`
convert $filename -fill black -draw "rectangle 1130,695 1270,715" -fill white -pointsize 15 -draw  "text 1135,710 '${timestamp:0:19}'" ./out.jpg

cp out.jpg /mnt/dav

----------------------------

i=0
for f in `ls -tr *.jpg 2>/dev/null`
do
  newf=`printf %06d $i`.jpg
  echo $f "-->" $newf
  mv $f $newf
  i=$((i+1))
done
avconv -r 10 -i %06d.jpg -r 10 -vcodec mjpeg -qscale 1  out.avi

-------------------------

mount -t davfs https://webdav.yandex.ru /mnt/dav -o uid=pi,gid=pi
cd /home/pi/mjpg-streamer && ./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"

curl http://localhost:8080/?action=snapshot > out.jpg

timestamp=`stat -c %y out.jpg`
convert out.jpg -fill black -fill white -pointsize 15 -draw  "text 5,15 '${timestamp:0:19}'" out_.jpg


