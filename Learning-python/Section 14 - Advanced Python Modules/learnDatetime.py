# Santosh Khadka
import datetime

myTime = datetime.time(2, 20)       # setting my own time. 2am 20minutes

# print(myTime.hour)
# print(myTime.minute)
# print(myTime.microsecond)       # will autoFill since I didn't assign it myself
# print(myTime)
# print(type(myTime))     # <class 'datetime.time'>

# today = datetime.date.today()
# print(today)        # 2021-09-20
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.ctime())

from datetime import datetime       # different from just "import datetime"
from datetime import date           # can also do datetime.date

# myDateTime = datetime(2021, 10, 3, 14, 20, 1)   # 2021-10-03 14:20:01
# print(myDateTime)                               # 2021-10-03 14:20:01
# myDateTime = myDateTime.replace(year=2020)      # 2021-10-03 14:20:01
# print(myDateTime)

## TIME MATH
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
date_x = date1-date2        # might have issues with leap years
print(date_x)
print(type(date_x))         # <class 'datetime.timedelta'>
print(date_x.days)          # just the days, can also do seconds, or total_seconds
