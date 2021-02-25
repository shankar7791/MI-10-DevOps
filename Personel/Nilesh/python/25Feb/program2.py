#Write a Python program to get the third side of right angled triangle from two given sides.
import math

side1 = float(input("enter the side1 : "))
side2 = float(input("enter the side2 : "))

side3 = math.sqrt(side1 ** 2 + side2 ** 2)

print("third side of right angled triangle is : ",side3)