# from time import sleep

# for i in range(1,5):
#     print(i,end="\t")
#     sleep(0.5)

# for x in range(10):
#     print '{0}\r'.format(x),
# print

# for x in range(10):
#     print("Progress {:2.1%}".format(x / 10), end="\r")

# last_x = ''
# for x in ['abc', 1]:
    
#     print()' ' * len(str(last_x)) + '\r'),
#     print '{}\r'.format(x),
#     last_x = x


import sys
from time import sleep
from datetime import datetime
for x in range(500):
    sys.stdout.write('\r'+str(datetime.now()))
    sleep(0.1)
    sys.stdout.flush()