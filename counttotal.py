import re
import string

frequency = {}
#initialise an empty dictionary to store frequency of each word

file1=raw_input('enter the name of file: ')
document_text = open(file1, 'r')
#opening file in read mode

text_string = document_text.read().lower()
#for regex simplicity, converting all to lower case

match_pattern = re.findall(r'\b[a-z]{1,20}\b', text_string)
#fin all occurences
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
#counter
     
frequency_list = frequency.keys()
#key-value pairs

 
for words in frequency_list:
    print words, frequency[words]
#print the frequency of each word
