#Write a Python program to get the third side of right angled triangle from two given sides.

side1 = float(input("Enter first side :- "))
side2 = float(input("Enter second side :-"))

side3 = ((side1 ** 2) + (side2 ** 2)) ** 0.5

print(f"The third side is :-", side3)

