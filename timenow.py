import sys
from datetime import datetime
from time import sleep

for x in range(100):
    sys.stdout.write('\r'+ str(datetime.now().year))
    sleep(0.1)
    sys.stdout.flush()