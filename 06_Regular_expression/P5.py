# Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
import re

list = ['aksh@gmail.com','@gmail.com','@','prachi012@gm.com']
for item in list:
    if re.match('[0-9a-zA-Z]+@',item):
        print(re.findall('[0-9a-zA-Z]+@',item))        