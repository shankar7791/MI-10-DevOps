num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))


if num1 > num2 and num1 > num3:
    print(f"{num1} is the Largest Number among three")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is the Largest Number among three")

else:
    print(f"{num3} is the Largest Number among three")