# Write a Python program to calculate the sum of a list of numbers using recursion.

# Algorithm

# def recur_factorial(n):
# if n == 1:
# return n.
# else:
# return n*recur_factorial(n-1)
# take input from the user.
# check is the number is negative.

def recur_fact(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_fact(n-1)  

num = int(input("Enter a number: "))  

if num < 0:  
   print("Invalid Number")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_fact(num))