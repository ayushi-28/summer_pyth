#!usr/bin/python2
import time
import datetime

print "Press1: to check current time   "

ch=raw_input()

if ch=='1':

   print "heyy"
   print time.ctime()
   print str(datetime.now())

else:

   print "return back"
