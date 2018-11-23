# To run any one unix cmd periodically (say every 1 hr once) using python
import os, subprocess, time
from datetime import datetime, timedelta
from subprocess import call

a = os.system('ls')
#print(a)


# while True:
#
#
# today = datetime.now()
# print("today",today)
# #
# one_hr = timedelta(hours=1)
# print(one_hr)

dt = datetime.now() + timedelta(hours=1)
print("dt",dt)
# dt = dt.replace(hour=1)
# print(dt)

while datetime.now() < dt:
     time.sleep(2)
     call('ls')

