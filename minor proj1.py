#!usr/bin/python2

import time
import os
import platform
import webbrowser
import commands
import requests
'''import scanip.scanip
import urllib2
import re'''

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from datetime import datetime

def getname():
	search_data=raw_input("Enter your data/:  ")
	final_data=search_data.strip()  #removing leading and trailing spaces
	done_data=final_data.split()    #splitting each word by space
        return done_data;

option ='''
press 1: enter any string and splitu each word and search on google
press 2:same but find list of all url on that website
press 3:same but find images url
press 4:current time and date
press 5:open default browser
press 6:all ip addresses in the ntwork
press 7:enter domain name  sand find list of ips, check owner, email and contact if available
'''
print option

ch=raw_input()

if ch== '1' :
	name=getname()
	for i in name:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)
		time.sleep(1)

elif ch=='2':
	
	name=getname()
	for i in name:
		#website=urllib2.urlopen('https://www.google.com/search?q='+i)
		resp=requests.get('https://www.google.com/search?q='+i)
		'''http_encoding=resp.encoding if 'charset' in resp.headers.get('content-type','').lower() else None
		html_encoding=EncodingDetector.find_declared_encoding(resp.content,is_html=True)
		encoding=html_encoding or http_encoding
		soup=BeautifulSoup(resp.content,from_encoding=encoding)
		
	for link in soup.find_all('a',href=True):
    		print(link['href'])'''
		data=resp.text
		soup=BeautifulSoup(data)
	for link in soup.find_all('a',href=True):
    		print(link.get('href'))


elif ch=='3':
	
	name=getname()

	for i in name:
		resp=requests.get('https://www.google.com/search?q='+i)
		cont=resp.content #used to get contents of the url opened
		soup=BeautifulSoup(cont,'lxml') #used to choose a parser and parse the content
		img_tags=soup.findAll('img') # this is used to search for all image tags on that page

	for img in img_tags:
		print(img.get('src'))	 

elif ch=='4':

	print str(datetime.now())

elif ch=='5':

	url='http://google.com'
	platform=platform.system()

 	if platform=='Linux':
		print 'linux'
		webbrowser.open_new_tab(url)
	elif platform=='Windows':
		print 'windows'
	 	webbrowser.open_new_tab(url)

elif ch=='6':

	print 'MY IP ADDRESS IS:'
	outtext=commands.getoutput("ifconfig wlp2s0 |head -2|tail -1| awk '{print $2}'")
	print outtext

	print 'Other IP in my network is'
	out=commands.getoutput("arp -a |cut -d'(' -f2|cut -d')' -f1")
	print out

elif ch=='7':

	name=str(getname())
	print 'list of IP addresses in the domain name:'
	dom=commands.getoutput('dig name +short A')
	print dom

	print 'details of dns ownern or admin'
	detail=commands.getoutput("whois adhocnw.org | grep -i 'Admin name\|admin email\|admin phone'")
	print detail
	
else:

	print 'no chance'




