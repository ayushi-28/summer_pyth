#!usr/bin/python2
import socket
import time

send_ip="127.0.0.1"
port_no=9007
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
s.bind((send_ip,port_no))

while 6<10:
	data=s.recvfrom(100)
	print "New message:  ",data[0]
	print "Client IP:   " ,data[1][0]
	reply= raw_input('Write your reply: ')
	s.sendto(reply,data[1])
