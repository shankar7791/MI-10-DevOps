# WAP TO calculate the sum of the list of nos using recursion.

def recur_sum(n):
if n < = 1:
    return n
else:
    return n + recur_sum(n-1)

n=10
if n < 0:
print(" Enter  positive number:")
else:
print(" The sum is": recur_sum(n))


# Alogrithm 
# create recursive function
# conditional statement
# print statment
# else statment
# take input from user
# conditional statement
# print statment
# else statment 
# function calling