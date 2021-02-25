# Program 4 : Write a Python program to calculate body mass index.
height = float(input("input your height in meters :"))
weight = float(input("input your weight in kilogram :"))
print("your body mass index is:",round(weight / (height * height),2))