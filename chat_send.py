#!/usr/python2
import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.connect(("127.0.0.1",9007))

while 6>2:
	msg=raw_input('Type your message here:')
	s.sendto(msg,("127.0.0.1",9007))
	time.sleep(1)
	d=s.recvfrom(100)
	print "New message from server:  ",d[0]
	print "Server IP:   " ,d[1][0]
