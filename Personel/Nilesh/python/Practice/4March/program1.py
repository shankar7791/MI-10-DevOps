#Write a Python function to sum all the numbers in a list.
def sum(numbers):

    total = 0 
    for i in numbers:
        total += i
    return total
    
print(sum([2,4,6,8,10,12,14,15]))