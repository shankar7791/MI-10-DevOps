#Write a Python function to sum all the numbers in a list.
list1 = [10 ,11,12,13,14,15]

def sum(n):
    sum1 = 0
    for i in n:
        sum1 += i

    return sum1
print(sum(list1))    