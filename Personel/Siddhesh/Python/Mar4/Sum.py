#Write a Python function to sum all the numbers in a list.

def Sum():

    lst = []
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number: '))
        lst.append(numbers)
    print("Sum of elements in given list is :", sum(lst))

Sum()