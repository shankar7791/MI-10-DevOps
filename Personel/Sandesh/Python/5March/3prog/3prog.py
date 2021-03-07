#Write a Python program to solve the Fibonacci sequence using recursion.

"""
1. take input from user
2. define function with it's parameter
2. Define the if condition as the number to be lesser than or equal to 1.
3. if condition is true exeute the statement
4. otherwise execute the else statement
5. Use a for loop and print the returned value which is the fibonacci series.
6. Exit.

"""

A = int(input("Enter number of terms:"))
print("Fibonacci sequence:")

def fibonacci(A):
    if(A <= 1):
        return A
    else:
        return(fibonacci(A-1) + fibonacci(A-2))

for i in range(A):
    print(fibonacci(i))