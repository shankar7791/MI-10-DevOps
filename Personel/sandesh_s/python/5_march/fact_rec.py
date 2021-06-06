# Write a Python program to get the factorial of a number using recursion


num = int(input("Enter Number : "))
def fact(num) :
    if num >= 1 :
        factorial = num * fact(num - 1)

    else :
        return 1

    return factorial
print(fact(num))
