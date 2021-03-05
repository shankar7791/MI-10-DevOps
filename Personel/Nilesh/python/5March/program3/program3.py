#Write a Python program to solve the Fibonacci sequence using recursion.

#algorithm:

#step-1 : get the terms of fibo as input from user into the variable.
#step-2 : send the length as parameter to recursive method which we named recur_fibo.
#step-3 : if the length is lesser than or equal to 1.
#step-4 : if the length is lesser or equal to 1 itss return immediately.
#step-5 : in else part it perform two recursive calls ( length -1 ) and (length - 2) to the function.
#step-6 : and last we call the function inside a for a loop which iterates fibo sequence and print the result.
#step-7 : STOP 

def recursive(length):
    if(length <= 1):
        return length
    else:
        return (recursive(length-1) + recursive(length-2))

length = int(input("Enter number of terms:"))

print("Fibonacci sequence using Recursion :")
for iter in range(length):
    print(recursive(iter)) 
