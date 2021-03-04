#Write a Python program function to print the even numbers from a given list.

def even(l):
    number = []
    for i in l:
        if i % 2 == 0:
            number.append(i)
    return number
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
