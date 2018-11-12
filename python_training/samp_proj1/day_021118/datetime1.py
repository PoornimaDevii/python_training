from datetime import datetime

from datetime import timedelta

start = datetime(2018,11,2)
print(start)
print(start + timedelta(12))
print(start - 2*timedelta(12))

from datetime import datetime
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta)
print(delta.days, delta.seconds)
