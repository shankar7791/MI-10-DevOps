#Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
print("Fizz is multiple of 3")
print("Buzz is multiple of 5")
print("FizzBuzz is multiple of 3 and 5")

i=1

while i<=50:
    if (i % 3 == 0 and i % 5 == 0):
        print(f"FizzBuzz:{i}")
    elif i % 3 == 0:
        print(f"Fizz:{i}")
    elif i % 5 == 0:
        print(f"Buzz:{i}")
    else:
        pass
    i=i+1
