#Python program function to print the even numbers from a given list.

n1=[15,42,40,85,96,80,34,50,55,12,23,24]

def even(n):
    for i in n:
        if i % 2 == 0:
            print(i, end=" ")

even(n1)

