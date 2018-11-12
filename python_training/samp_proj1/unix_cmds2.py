# ctrl+C operation to be changed (in unix)

import signal
import time

def handler(a,b):
    print("Signal Number",a, "frame",b)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

signal.signal(signal.SIGINT, handler)
while True:
    print("not afraid of C-c")
    time.sleep(1)