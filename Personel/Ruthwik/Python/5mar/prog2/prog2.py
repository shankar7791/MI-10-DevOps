#Python program to get the factorial of a number using recursion

# Algorithm :
# step 1 : input the number
# step 2 : define the function
# step 5 : if n==1
#             return n
#          else
#             return n*factorial(n-1)
# step 4 : if num < 0
#             print enter positive no
#          elif num == 0
#             print The factorial of 0 is 1
#          else
#             print factorial and call recursive function


def factorial(n):  
    if n == 1:  
       return n  
    else:  
       return n*factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("enter positive numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",factorial(num))  