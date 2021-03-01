#program to print the fibonacci sequence
terms = int(input("enter the terms : "))
a,b = 0, 1
count = 0
if terms <= 0:
    print("enter a positive integer")
elif terms == 1:
    print("fibonacci sequence upto : ",terms,":")
    print(a)
else:
    print("fibonaci sequence : ")
    while count < terms:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1