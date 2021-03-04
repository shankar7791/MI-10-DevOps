#Check the number is prime or not

def prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

num=int(input("Enter the number: "))
prime(num)    