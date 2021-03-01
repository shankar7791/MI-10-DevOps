# Program 2 : write a program for Fibonacci series

terms = int(input("Enter the terms : "))
n1 = 0
n2 = 1
count = 0

while count < terms:  
    print(n1)
    nextTerm = n1 + n2
    n1 = n2
    n2 = nextTerm
    count += 1