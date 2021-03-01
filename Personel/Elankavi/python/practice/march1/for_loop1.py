# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 
for i in range(1500,2700):
    if(i%7==0):
        print("The number is divisible by 7 : ",i)
    else:

        print("The number is multiple by 5 : ",i*5)