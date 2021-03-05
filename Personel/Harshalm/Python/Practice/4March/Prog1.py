#Write a Python function to sum all the numbers in a list. 


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum((7, 3, 8, 9, 2, 0, 1))) 

