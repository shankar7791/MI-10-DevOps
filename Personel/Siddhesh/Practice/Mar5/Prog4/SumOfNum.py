#Python program to find the sum of sequence of all numbers upto the given number using recursive function.

#step-1: take a input from user 
#step-2: define the function as recur_sum.
#step-3: check if n is less than or equal to 1 then return n.
#step-4: otherwise go to else part and return n + and call recursive method(n-1).
#step-5: call the function and print the result.

 
n = int(input("enter the number : "))
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

print(recur_sum(n))

