# Write a Python program to extract year, month, date and time using Lambda.
#  Sample Output:
#  2020-01-15 09:03:32.744178
#  2020
#  1
#  15
#  09:03:32.744178
 

from datetime import datetime

currentDateTime = datetime.now()

timeAnddate = lambda currentDateTime : currentDateTime
print(timeAnddate(currentDateTime))

timeAnddate = lambda currentYear : currentYear.year
print(timeAnddate(currentDateTime))

timeAnddate = lambda currentMonth : currentMonth.month
print(timeAnddate(currentDateTime))

timeAnddate = lambda currentDay : currentDay.day
print(timeAnddate(currentDateTime))

timeAnddate = lambda currentTime : currentTime.time()
print(timeAnddate(currentDateTime))