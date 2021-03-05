# Program 1 : Write a Python program to calculate the sum of a list of numbers using recursion.
def recursion_sum(data):
    total = 0
    for element in data:
        if type(element) == type([]):
            total = total + recursion_sum(element)
        else:
            total = total + element

    return total


print(recursion_sum([1, 2, [3, 4], [5, 6]]))


# ALGORITHM
# 1 take input from user in function
# 2 declare function
# 3 using for loop element is called
# 4 checking condition
# 5 store addition in total with adding total and user input
# 6 else total + given input
# 7 finally tatal is return
