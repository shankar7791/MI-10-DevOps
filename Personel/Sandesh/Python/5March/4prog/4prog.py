# Python program to find the sum of sequence of all numbers upto the given number using recursive function
"""
1. take input from user
2. define function and it's argument
3. define the if statement if it's true execute it
4. otherwise execute else statement
5. print statement

"""

num = int(input("Enter a number: "))

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
print("The sum is: ", sum(num))


