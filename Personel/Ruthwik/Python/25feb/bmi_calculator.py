#Python program to calculate body mass index.

h = float(input('Enter your height in meter:'))
w = int(input('enter your weight in kg:'))

bmi =round( w / (h ** 2),2)

print(f'Your BMI index is: {bmi}')