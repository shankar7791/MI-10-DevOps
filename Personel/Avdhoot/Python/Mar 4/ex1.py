#Write a Python function to sum all the numbers in a list.

def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
print(sum((10,30,20,1,12,4)))