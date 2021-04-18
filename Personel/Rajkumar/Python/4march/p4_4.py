#Write a Python function that takes a number as a parameter and check the number is prime or not.

#declare a Function
def prime(number):
# prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
         if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
             print(number, "is a prime number")

# if the entered number is less than or equal to 1
    else:
        print(number, "is not a prime number")

# taking input from user
number = int(input("Enter any number: "))
#calling a Function
prime(number)