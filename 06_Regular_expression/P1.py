# Write a regular expression to search digits inside a string
import re

string = 'aksh012-git012'
regxObj = re.compile('[0-9]+')
print(regxObj.findall(string))

