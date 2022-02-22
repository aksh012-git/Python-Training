# Write a Python program to extract year, month, date and time using Lambda.
#  Sample Output:
#  2020-01-15 09:03:32.744178
#  2020
#  1
#  15
#  09:03:32.744178
 

from datetime import datetime

current = datetime.now()

timeAnddate = lambda x : x
print(timeAnddate(current))

timeAnddate = lambda x : x.year
print(timeAnddate(current))

timeAnddate = lambda x : x.month
print(timeAnddate(current))

timeAnddate = lambda x : x.day
print(timeAnddate(current))

timeAnddate = lambda x : x.time()
print(timeAnddate(current))