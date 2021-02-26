# Program 5 : Write a Python program to get the system time.

import datetime



# from datetime import datetime

#Get Current Date and Time
# datetime_object = datetime.datetime.now()
# print(datetime_object)

time = datetime.datetime.now().time() 
print("Current System Time =", time) 