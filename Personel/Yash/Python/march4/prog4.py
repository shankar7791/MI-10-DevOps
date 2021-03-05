# # Program 4 : Write a Python function that takes a number as a parameter and check the number is prime or not. 


def checkPrime(num):
    count=0
    for i in range(1,num+1):
        if (num % i) == 0:
            count+=1
    if count == 2 :
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

num=int(input("Enter the number : "))
checkPrime(num)