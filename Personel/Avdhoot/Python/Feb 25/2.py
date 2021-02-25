#Write a Python program to get the third side of right angled triangle from two given sides

a = int(input("Enter First side "))
b = int(input("Enter Second side "))

c = a ** 2
d = b ** 2

e = c + d

f = e ** (1/2)
print(f)