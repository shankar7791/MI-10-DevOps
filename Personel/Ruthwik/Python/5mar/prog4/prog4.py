#Python program to find the sum of sequence of all numbers upto the given number using recursive function

# Algorithm :
# step 1 : input the number
# step 2 : define the function
# step 5 : if n<=1
#             return n
#          else
#             return n+r_sum(n-1)
# step 4 : if num < 0
#             print enter positive no
#          else 
#             print sum and call recursive function 


def r_sum(n):
    if n <= 1:
       return n
    else:
       return n + r_sum(n-1)

# change this value for a different result
num = int(input("Enter the number : "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",r_sum(num))