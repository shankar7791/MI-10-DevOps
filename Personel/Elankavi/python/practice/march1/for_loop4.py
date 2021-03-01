# Write a Python program that prints all the numbers from 0 to 20 except divisible by 5 and 4
for i in range(0,20):
    if(i % 5==0) or (i % 4==0):
        continue
    print(i)