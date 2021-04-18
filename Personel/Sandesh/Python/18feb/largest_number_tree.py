num1 = float(input("Enter the First Number : "))
num2 = float(input("Enter the Second Number : "))
num3 = float(input("Enter the Third Number : "))
if (num1 > num2) and (num1 > num3) :
    large = num1
    print(large, "the Largest Number is : ")
elif (num2 > num1) and (num2 > num3) :
    large = num2
    print(large, "the Largest Number is : ")
else :
    large = num3 

    print(large, "the Largest Number is : ")