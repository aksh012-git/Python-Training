# Replace all special characters with space using regex
import re

string = 'ak-sh@gmail.com?'
my_new_string = re.sub('[^a-zA-Z0-9]', ' ', string)
print(my_new_string)