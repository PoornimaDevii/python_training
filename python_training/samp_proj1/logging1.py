# Logging file example

import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
filename=LOG_FILENAME,
    level=logging.DEBUG)

logging.critical('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)
print(logging.__file__)