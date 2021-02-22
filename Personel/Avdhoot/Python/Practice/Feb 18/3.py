#Nested if....else

x = int(input("Enter the Marks "))

if x <= 50:
    if x <= 34:
        print("Fail")
    else:
        print("pass")
else :
    if x >= 70 :
        print("Pass with distinction")
    else :
        print("First Class")
