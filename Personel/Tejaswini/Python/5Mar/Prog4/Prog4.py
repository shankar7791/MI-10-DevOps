#Algorithm
#1. Define function  
#2. Take user integer input
#3. Call the function and pass user input as argument
#4. True condtion if n is less than or equal to 1 then,
#   return n to function and goto step 5  otherwise, 
#   Flase condition: else return n add recursivefun() call with decrease n variable and goto step 4
#5. Print the result 

def sum1(n):
    if n <= 1:
        return n
    else:
        return n + sum1(n - 1)

num = int(input("Enter the number : "))
print("The sum of sequence of all no upto n :  ",sum1(num))