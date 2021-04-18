
# WAP TO sum of sequence of all nos upto the given no using recursion function.

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)


num = 25 # take input from user 
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
   
   # Alogrithm
   # create sum function
   # conditional statemnet
   # print statment
   # else statment 
   # take input from user
   # print positive no
   # else statment
   # print recur sum no