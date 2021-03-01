#write a program for Fibonacci series. 
num = int(input("enter the number : "))
a = 0
b = 1
c = 1
sum = 0
while (c<=num):
    c = c +1
    a = b
    b = sum
    sum = a + b
    print(f"{sum} fibonacci series is : ")
    