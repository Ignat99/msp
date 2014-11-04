# MSP - Minecraft system project 

## Installation

Make image of Rasbian on MicroSD for Raspberry Pi B+.

* [raspberrypi.org - Linux install](http://www.raspberrypi.org/documentation/installation/installing-images/linux.md)

Insert MicroSD. Connected power. Connected network cable to router.

     ifconfig | grep Bcast
          inet addr:192.168.0.103  Bcast:192.168.0.255  Mask:255.255.255.0


     nmap -sn 192.168.0.103/24

     Nmap scan report for 192.168.0.117
     Host is up (0.00050s latency).
     MAC Address: XX:XX:XX:XX:XX:XX (Raspberry Pi Foundation)

* [SSH (SECURE SHELL)](http://www.raspberrypi.org/documentation/remote-access/ssh/)

Default  username: pi and password: raspberry.

     ssh -l pi 192.168.0.117
     
     sudo raspi-config
     
* [Raspi wifi setup](http://www.raspberrypi.org/forums/viewtopic.php?t=26795)
* [Raspi reboot command](http://www.raspberrypi.org/forums/viewtopic.php?f=28&t=73121)

     sudo shutdown -r now
     
If you don't have dhcp on you router (like mobile phone), need change nameserver in /etc/resolv.conf:

* [DNS setup](http://www.raspberrypi.org/forums/viewtopic.php?f=63&t=17016)


     sudo nano /etc/resolv.conf
     
     nameserver 8.8.8.8
     
     nameserver 8.8.4.4
     
* [Road trip raspberry pi](http://www.cyborgworkshop.org/2014/08/07/road-trip-raspberry-pi/)

## Dependencies

* [Node-RED - MQTT interface](https://github.com/node-red/node-red)
* [Mosquitto - An Open Source MQTT Broker](http://mosquitto.org/) 
* [Emoncms - Open-source energy visualisation](http://emoncms.org/)
or [DashUI](https://github.com/hobbyquaker/DashUI)
* [Node-RED-nodes-Emoncms](https://github.com/node-red/node-red-nodes/tree/master/io/emoncms)

## Install MSP API

    git clone https://github.com/Ignat99/msp.git
    cd msp/
    git fetch upstream
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    git checkout -b my_feature
    
Your additions can be sent by the command:

    git checkout -b feature
    
    

## Install TheThingSystem

* [TheThingSystem - Raspberry Pi B+](https://github.com/TheThingSystem/steward/wiki/Bootstrapping-the-Raspberry-Pi)

     sudo apt-get update

     sudo apt-get upgrade

## Install Node-RED

* [nodered.org - Raspberry Pi B+](http://nodered.org/docs/hardware/raspberrypi.html)

## Hardware

* [A single LED](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/)
* [TheThingSystem - Arduino - LED](https://github.com/TheThingSystem/steward/wiki/Clients)
* [Thing Sensor Reporting Protocol - Arduino - Weather Station](https://github.com/TheThingSystem/steward/wiki/Thing-Sensor-Reporting-Protocol)
* [Parrot Flower Power](http://www.parrot.com/de/produkte/flower-power/)

## Protocols

* [Simple-Thing-Protocol](https://github.com/TheThingSystem/steward/wiki/Simple-Thing-Protocol)
* [P2P net from TAAS-server](https://github.com/TheThingsystem/TAAS-server)
* [P2P net OpenBazaar](https://github.com/OpenBazaar/OpenBazaar)

Your first step is to go to the [the wiki](https://github.com/Ignat99/msp/wiki). Enjoy!
