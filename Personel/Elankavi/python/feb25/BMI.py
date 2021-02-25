#program to calculate the BMI

h = float(input("Enter your height in meter: "))
w = float(input("Enter your weight in kg: "))
bmi = w/(h ** 2)
print(f"Your BMI is ",bmi)