#Write a Python program function to print the even numbers from a given list. 


list = [12,54,23,76,98,34,64,87,13,45,88,66,56]

def even(num) :
    for i in num :
        if i % 2 == 0 :
            print(i)
even(list)