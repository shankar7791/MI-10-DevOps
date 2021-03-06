# Program 3 :  Write a Python program to solve the Fibonacci sequence using recursion.

'''
Algorithm :
step 1 : input the number
step 2 : define the function
step 5 : if n<=1
            return n
         else
            return fibo(n-1) + fibo(n-2)
step 4 : if num <= 0
            print Enter the no of terms greater than 0 
         else 
            print call recursive function 

'''

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

num=int(input("Enter the number of terms : "))
if num <= 0:
   print("Enter the no of terms greater than 0 ")
else:
   for i in range(num):
       print(fibo(i))

