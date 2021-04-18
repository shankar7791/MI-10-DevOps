#Write a Python program function to print the even numbers from a given list

list=[11,84,15,40,32,54]
def even(list):
    for x in list:
        if x%2==0:
            print(x)
even(list)