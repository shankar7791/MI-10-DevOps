#Python program to get the system time.

from datetime import datetime

d = datetime.now()

current_time = d.strftime("%H:%M:%S")

print("Current Time : ", current_time)