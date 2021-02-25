#Write a Python program to calculate body mass index.

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
a = weight / (height * height)
print("Your body mass index is: ", round(a, 2))