#Write a program for Fibonacci series.

n = int(input("Enter the Range : "))
a = int(input("Enter the Starting number : "))
b = int(input("Enter the Second number : "))
c = 1
sum = 0

print("Fibonacci series\n")

while (c <= n):
    print(sum, end=" ")
    c += 1
    a = b
    b = sum
    sum = a + b