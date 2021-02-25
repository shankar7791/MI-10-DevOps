#Python program to get the third side of right angled triangle from two given sides.

a=int(input("Enter side a :"))
b=int(input("Enter side b :"))

c = ((a**2)+(b**2))**0.5

print("The third side is : ", round(c))