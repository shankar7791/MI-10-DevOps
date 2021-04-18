#Write a Python program to solve the Fibonacci sequence using recursion. 

    #****Algorithm****
    #1.Take a Take a Input of User
    #2.Define the function
    #3.if n<=1
    #4.     return n
    #5. else:
    #6.     return rfibonacci(n-1) + rfibonacci(n-2)
    #7.If user enter a negative Number than print "Plese enter a positive integer"
    #8.other vice performing task and print output
def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))
n1 = int(input("Enter a number : "))
if n1<= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n1):
       print(fibo(i)) 

    
  

