#!usr/bin/python2

name=raw_input("Enter the name of your file:  ")
file1=open(name,'r') 
data=file1.read()
file1.close()
#opening the file in read mode

words=data.split(" ")
print "\n"
print words
#Breaking a string using a " "separator


unique=list(set(words))
print "\n"
print unique
#Removing multiple presence of same words

for i in unique:
	if unique[i]==words[i]:
		cnt=words.count(i)
        print i,cnt
#occurence of each word in a line
