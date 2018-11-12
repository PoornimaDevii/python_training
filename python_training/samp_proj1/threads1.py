# a process can have one or more threads.
# threads share the same data always

import _thread
import time

def print_time(delay):
    while True:
        time.sleep(delay)
        print(time.ctime(time.time()))

_thread.start_new_thread(print_time, (5,))
while True:
    pass