import time
ct1=time.ctime()
print(f"Current Calender {ct1}")
print()
t = time.localtime()
ct= time.strftime("%H:%M:%S", t)
print(f"Current Time = {ct}")