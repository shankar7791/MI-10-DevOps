#Algorithm
#1. Define function  
#2. Take user integer input
#3. Call the function and pass user input as argument
#4. True condtion if n is less than or equal to 1 then,
#   return n to function and goto step 5  otherwise, 
#   Flase condition: else return  add using recursivefun() previous number to next number until num greater than 1 and goto step 1
#5. Print the result using loop

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return (recur_fibo(n-1) + recur_fibo(n-2))

n = int(input("Enter the input number: "))

print("Fibonacci sequence:")
for i in range(n):
    print(recur_fibo(i))
