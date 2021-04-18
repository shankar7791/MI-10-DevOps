#Write a Python program to calculate body mass index.

height = float(input("Enter your height in meter :-"))
weight = float(input("Enter your weight in  kg :-"))

bmi = (weight /(height * height))

print("your BMI is :-", bmi)

