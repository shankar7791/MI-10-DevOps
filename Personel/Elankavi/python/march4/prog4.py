#python function that takes a number as a parameter and check the number is prime or not :

def prime(n):
    if(n < 2):
        return False
    for i in range(2, n // 2+1):
        if n % i == 0:
            return False

    return True


no = int(input("enter numbers:"))
if prime(no):
    print(no, "is Prime")
else:
    print(no, "is not a prime")