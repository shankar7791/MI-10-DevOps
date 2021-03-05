# Program 3 :  Write a Python program to solve the Fibonacci sequence using recursion.

def fibonaccies(n):
    if n <= 1:
        return n
    else:
        return (fibonaccies(n-1)+fibonaccies(n-2))


n = int(input("enter value :"))
print("fibonaccies sequence")
for i in range(n):
    print(fibonaccies(i))


# ALGORITHM
# 1 take input from user and store it in variable
# 2 number pass as a argument
# 3 check condition number is less than 1
# 4 function recursively called an argument as number minus 1
# 5 the result returned
# 6 for is used to print fibbo
