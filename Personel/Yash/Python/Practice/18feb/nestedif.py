#nested if
num = int(input("Enter a number: "))

if num <= 0:
    if num == 0:
        print("Entered number is zero")
    else:
        print("Entered number negative number")
else:
     print("Entered number positive number")