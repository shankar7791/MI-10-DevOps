# Python program to find the sum of sequence of all numbers upto the given number using recursive function

# Algorithm

# define function passing parameter
# if condition  if n <= 1
# return n
# Test else condition when if condition is false
# retun n + recur_sum(n-1)
# Take the input from User
# Test the If condition for positive number if num < 0
# Else print the called function using argument


def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)


num = int(input("Enter the Number: "))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))
