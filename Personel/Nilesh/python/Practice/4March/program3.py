#Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("the number is not prime")
                break
        else:
            print("the number is prime")
    else:
        print("number is not prime")

prime(5)