#Write a Python program to solve the Fibonacci sequence using recursion.
def fib(n):
    n1=0
    n2=1
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

num=int(input("enter the number"))
if num<=0:
    print("number is negitive")
else:
    for i in range(num):
        print(fib(i))


#Algoritham
#define a function def fib(n)
#deine n1=0 and n2=1
#check if n<=1
#return n
#else,return (fib(n-1)+fib(n-2))
#take input from user
#check if num<=0
#print number is negative
#else take a for loop
#then print and goto step1