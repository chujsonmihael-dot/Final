import sys
from time import sleep
time = 0
while time < 30:
    sys.stdout.write("\rLoading.  ")
    sleep(0.5)
    sys.stdout.write("\rLoading.. ")
    sleep(0.5)
    sys.stdout.write("\rLoading...")
    sleep(0.5)
    time+=1