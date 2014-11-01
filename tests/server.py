#!/usr/bin/python
# Source code: http://habrahabr.ru/post/234939/
# Test server code for Raspberry Pi
# Written in Python 2.7.3
import socket, select
import RPi.GPIO as GPIO
import time
#Функция посылает один бит данных к контролеру
def sendBit(pinState):
    if pinState==0:
                GPIO.output(pinData, 0)
    else:
                GPIO.output(pinData, 1)         
    GPIO.output(pinClock, 0)
    time.sleep(sleepInterval)
    GPIO.output(pinClock,1)
    time.sleep(sleepInterval)

#Функция посылает массив данных на компьютер
def sendArray(args):
    GPIO.setmode(GPIO.BCM) # эту настройку нумерации пинов надо перенести перед определением номеров пинов
    #инициализация пинов,не изменяя состояние (должно оставатся 1)
            GPIO.setup(pinData,GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(pinClock,GPIO.OUT, initial=GPIO.HIGH)
    #посылаю 0 бит
    GPIO.output(pinData, 0)         
    GPIO.output(pinClock, 0)
    time.sleep(sleepInterval)
    GPIO.output(pinClock,1)
    time.sleep(sleepInterval)
    #Посылаю полученный массив данных
    for v in args:
                sendBit(v)
    #Посылаю стоп-бит
    GPIO.output(pinData, 1)
    GPIO.output(pinClock, 0)
    time.sleep(sleepInterval*2)
    GPIO.output(pinClock,1)
    time.sleep(sleepInterval*200)
    GPIO.cleanup()

pinClock=4
pinData=15
sleepInterval=0.00020
CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 8928     
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)
CONNECTION_LIST.append(server_socket)
print "Готов принимать данные на порту " + str(PORT)
while 1:
    read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
    for sock in read_sockets:
                if sock == server_socket:
                           sockfd, addr = server_socket.accept()
                           CONNECTION_LIST.append(sockfd)
                else:                            
                           try:
                                       data = sock.recv(RECV_BUFFER)                                        
                                       i=0
                                       scanCode=[]
                                       print "Принял данные:"+data
                                       for bukva in data:
                                                   if bukva=="1":
                                                               scanCode.append(int(1))                                                                   
                                                   else:
                                                               scanCode.append(int(0))        
                                                   i=i+1
                                       sendArray(scanCode)
                                       sendArray([0,0,0,0,1,1,1,1,1])
                                       sendArray(scanCode)
                                        sock.close()
                                       CONNECTION_LIST.remove(sock)  
                           except:
                                       sock.close()
                                       CONNECTION_LIST.remove(sock)
                                               continue

server_socket.close()
