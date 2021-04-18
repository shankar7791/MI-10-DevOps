#find the greatest number among the three number

num1= float(input("Enter the 1st number : "))
num2= float(input("Enter the 2nd number : "))
num3= float(input("Enter the 3rd number : "))
if(num1 > num2) and (num1 > num3):
    print(num1, "is the largest number")
elif(num2>num1) and (num2>num3):
    print(num2,"is the largest number ")
else:
    print(num3, "is the largest number")