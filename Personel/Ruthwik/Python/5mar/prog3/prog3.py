#Python program to solve the Fibonacci sequence using recursion.

# Algorithm :
# step 1 : input the number
# step 2 : define the function
# step 5 : if n<=1
#             return n
#          else
#             return rfibonacci(n-1) + rfibonacci(n-2)
# step 4 : if num <= 0
#             print Enter the no of terms greater than 0 
#          else 
#             print call recursive function 


def rfibonacci(n):
    if n <= 1:
       return n
    else:
       return(rfibonacci(n-1) + rfibonacci(n-2))

nterms = int(input("Enter a number : "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(rfibonacci(i))