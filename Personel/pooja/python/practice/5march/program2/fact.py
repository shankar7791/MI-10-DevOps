# Program 2 :  Write a Python program to get the factorial of a number using recursiond
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


n = int(input("enter the n value :"))
res = factorial(n)
print(res)


# ALGORITHM
# 0 declare function
# 1 function waiting for input
# 2 take input from user in function
# 3 checking condition and it is true it will return 1
# 4 else part is for fact condition
# 5 finally res stored output
# 6 printing res
