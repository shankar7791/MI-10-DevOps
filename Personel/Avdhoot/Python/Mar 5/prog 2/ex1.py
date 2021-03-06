#Write a Python program to get the factorial of a number using recursion
'''
Algorithm
1. Define a Funtion
2. Write if condition as if input is 0 or 1 th factorial is 1
3. Write else condition + recursion
4. Take the input from user and print the result
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)

print(factorial(int(input("Enter the Number: "))))