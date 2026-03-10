import datetime

date1 = datetime.datetime(2020, 6, 18, 12, 30, 00, 500000) 
date2 = datetime.datetime(2021, 6, 18, 13, 30, 00, 400000)

res = date2 - date1
print(type(res))
print(res.seconds)
print(res.days)
print(res.microseconds)
print(res.total_seconds())
# datetime is a module in the Python standard library that provides classes for working with dates and times. 
# The datetime class is a combination of a date and a time. 
# It has attributes for year, month, day, hour, minute, second, and microsecond. 
# You can create a datetime object by passing the year, month, day, and optionally the hour, minute, second, and microsecond to the datetime constructor. 
# You can perform arithmetic operations on datetime objects, such as subtraction, which returns a timedelta object. 
# The timedelta object has attributes for days, seconds, and microseconds, and a method total_seconds() that returns the total number of seconds contained in the duration.