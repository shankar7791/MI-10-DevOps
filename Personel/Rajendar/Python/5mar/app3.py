# Write a Python program to solve the Fibonacci sequence using recursion.

# Algorithm
# define a function passing a parameter
# Test the condition using the If statement if n <= 1
# If true the return n
# Test else condition when if condition is false and return(r_fibo(n-1) + r_fibo(n-2))
# Take an Input from user for n term
# Test if condition for positive number if n <= 0
# Print else statement
# Using for loop for the range of n terms
# print the called function by using an argument

def r_fibo(n):
    if n <= 1:
        return n
    else:
        return(r_fibo(n-1) + r_fibo(n-2))


n = int(input("Enter the Number: "))

if n <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(r_fibo(i))
