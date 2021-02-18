#nested if statement
#Nested-if statement :-nested if statement means an if statement inside another if statement.

num = int(input("Enter a number:-"))
if num <= 100 :
    if num < 50 :
        print("Num is less than 50")
    else :
        print("Num is greater than 50")
else :
    if num > 100 :
        if num > 75 :
            print("Num is greater than 100")
        else :
            print("Num is less than 75")
    else :
        print("Num is greater than 100")

