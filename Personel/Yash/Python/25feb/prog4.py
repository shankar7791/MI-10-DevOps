# Program 4 : Write a Python program to calculate body mass index.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi=round(weight / (height * height),3)

print("Your body mass index is: ",bmi)