num = int(input("How many terms? "))

a, b = 0, 1
count = 0

if num <= 0:
    print("Please enter a positive integer")
elif num == 1:
    print("Fibonacci sequence upto", num, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < num:
        print(a)
        sum = a + b
        a = b
        b = sum
        count += 1
