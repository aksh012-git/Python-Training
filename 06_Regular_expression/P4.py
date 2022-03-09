# Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
import re

listWithString = ['aksh12;','maradiya;','kshitij;:','prachi;']
for item in listWithString:
    if re.match('[0-9a-zA-Z]+;$',item):
        print(item)
        