# Write a Python program to count the number of even and odd numbers from a series of numbers
n=(1,2,3,4,5,6,7,8,9)
count=0
count2=0
for i in n:
    if(i%2==0):
        count+=1
    else:
        count2+=1
print("No of odd number you enter : ",count)
print("No of even number you enter : ",count2)