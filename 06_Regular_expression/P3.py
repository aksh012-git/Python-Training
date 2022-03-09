# Find the numbers starting with 212 from a string.
import re

string ='212000 aksh012-git 34021245 mak212 2129'
findString212 = re.findall(r'\b212\d+',string)
print(findString212)