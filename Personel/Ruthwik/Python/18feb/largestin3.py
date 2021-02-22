# Python program to find the largest number among the three numbers

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

if (a >= b) and (a >= c) :
    l = a
elif (b >= a) and (b >= c) :
    l = b
else :
    l = c

print(f"{l} is the largest number")