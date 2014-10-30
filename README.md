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
     MAC Address: B8:27:EB:20:25:2E (Raspberry Pi Foundation)

* [SSH (SECURE SHELL)](http://www.raspberrypi.org/documentation/remote-access/ssh/)

 user: pi
 password: raspberry

     ssh -l pi 192.168.0.117
     sudo raspi-config

* [TheThingSystem - Raspberry Pi B+](https://github.com/TheThingSystem/steward/wiki/Bootstrapping-the-Raspberry-Pi)
* [nodered.org - Raspberry Pi B+](http://nodered.org/docs/hardware/raspberrypi.html)

## Hardware

* [A single LED](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/)
* [TheThingSystem - Arduino - LED](https://github.com/TheThingSystem/steward/wiki/Clients)
* [Thing Sensor Reporting Protocol - Arduino - Weather Station](https://github.com/TheThingSystem/steward/wiki/Thing-Sensor-Reporting-Protocol)
* [Parrot Flower Power](http://www.parrot.com/de/produkte/flower-power/)

## Dependencies

* [Node-RED - MQTT interface](https://github.com/node-red/node-red)
* [Mosquitto - An Open Source MQTT Broker](http://mosquitto.org/) 
* [Emoncms - Open-source energy visualisation](http://emoncms.org/)
or [DashUI](https://github.com/hobbyquaker/DashUI)
* [Node-RED-nodes-Emoncms](https://github.com/node-red/node-red-nodes/tree/master/io/emoncms)

## Protocols

* [Simple-Thing-Protocol](https://github.com/TheThingSystem/steward/wiki/Simple-Thing-Protocol)
* [P2P net from TAAS-server](https://github.com/TheThingsystem/TAAS-server)
* [P2P net OpenBazaar](https://github.com/OpenBazaar/OpenBazaar)

Your first step is to go to the [the wiki](https://github.com/Ignat99/msp/wiki). Enjoy!
