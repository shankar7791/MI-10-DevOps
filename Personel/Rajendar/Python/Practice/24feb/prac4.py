# Relational opeartor and Logical operator
# program to read marks and find the grade using relational operator


marks = int(input("Enter the Marks "))
if marks < 0 or marks > 100:
    print("Marks is not in range")

elif marks >= 70:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
