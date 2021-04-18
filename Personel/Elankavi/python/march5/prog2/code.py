# program to find the sum of sequence of all numbers upto the given number using the recursive function:

# Algorithm
# : Assign the function as recursion:
# :take input from user
# :Using the conditional statement
# :If condition is true execute the if statement
# :else execute the else statement
# :Return the i value and print

def recursion(i):
    if(i<=0):
        return i
       
        
    else:
        return(i + recursion(i-1))
i=int(input("Enter the last digit : "))
recursion(i)
print("The sum is",recursion(i))

