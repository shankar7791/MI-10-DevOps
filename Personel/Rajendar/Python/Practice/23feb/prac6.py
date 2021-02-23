# Program 6 : Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

i = 1

print("Print Fizz if Number is multiple of 3:")
print("Print Buzzif Number is multiple of 5:")
print("Print FizzBuzz if Number is multiple of 5 and 3:")

while i <= 50:
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        pass
    i = i+1
