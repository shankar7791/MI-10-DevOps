# Program 2 :  Write a Python program to get the factorial of a number using recursion
'''
Algorithm :
step 1 : input the number
step 2 : define the function
step 5 : if n==1
            return n
         else
            return n*factorial(n-1)
step 4 : if num < 0
            print enter positive no
         elif num == 0
            print The factorial of 0 is 1
         else
            print factorial and call recursive function 
'''
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num=int(input("Enter the number : "))
if num < 0:
   print("Enter the positive number")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print(f"The factorial of {num} is {factorial(num)}")



