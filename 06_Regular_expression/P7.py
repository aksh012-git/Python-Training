# Replace the space character that occurs after a word ending with a or r with a newline character
# Sample input: area not a _a2_ roar took 22
# Sample output:
# area
# not a
# _a2_ roar
# took 22

import re

string = "area not a _a2_ roar took 22"
find_lst = re.findall(r'\b[A-Za-z]*a\b|\b[A-Za-z]*r\b',string)
string_lst = string.split(' ')
strConcat = ''
for item in string_lst:
    strConcat = strConcat + item + ' '
    if item in find_lst:
        strConcat = strConcat + '\n'
print(strConcat)   

