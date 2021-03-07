#Algorithm
#1. Take user integer input 
#2. Define function 
#3. Call the function and pass user input as argument
#4. True condtion if n is less than or equal to 1 then,
#   return n to function and goto step 5  otherwise, 
#   Flase condition: else return num multiply recursivefun() call with decrease n variable and goto step 1 ultil num > 1
#5. Print the result 

num = int(input("Enter Number: "))

def Fact(num):
   if num > 1:
       return num*Fact(num-1)
   else:
       return num

print("Factorial of Number = ", Fact(num))
    