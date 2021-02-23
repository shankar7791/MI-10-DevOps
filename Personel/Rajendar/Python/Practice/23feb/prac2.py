# Program 2 : Write a Python program to construct the following pattern, using a nested while loop.*
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


n = int(input('Enter number of rows : '))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
i = 0
while i <= n:
    j = n
    while j >= i:
        print("*", end=" ")
        j -= 1
    print()
    i += 1
