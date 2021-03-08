
# Write a Python program to get the factorial of a number using recursion

# Algorithm

# 1. take a inpute from user
# 2. defining function 
# 3. give condition to check number is >= 1 
# 4. re-call function upto the condition gets false
# 5. print the result when condition false using function call



num = int(input("Enter Number : "))
def fact(num) :
    if num >= 1 :
        factorial = num * fact(num - 1)

    else :
        return 1

    return factorial       
print(fact(num))