a=int(input("Enter the number below 50"))
b=int(input("Enter the number above 50"))

#IF statement
if a < b :
    print("a is less than b")

#IF...Else statement
if a > b :
    print(f"{a} is greater than {b}")
else :
    print(f"{b} is greater than {a}")

#Nested IF statement
if a < 20 :
    print(f"{a} is less than 20")
    if a < 40 :
        print(f"{a} is less than 40")
        if a < 60 :
            print(f"{a} is less than 60")
            if a < 80 :
                print(f"{a} is less than 80")
                if a < 100 :
                    print(f"{a} is less than 100")
                else :
                    print(f"{a} is greater than 100")
            else :
                print(f"{a} is greater than 80")
        else :
            print(f"{a} is greater than 60")
    else :
        print(f"{a} is greater than 40")
else :
    print(f"{a} is greater than 20")

#IF...ELIF statement
if a < b:
    print(f"{a} is less than {b}")
elif a == b :
    print(f"{a} is equal to {b}")
else :
    print(f"{a} is greater than {b}")

#Shorthand IF statement
if a < b : print(f"{a} is less than {b}")

#Shorthand IF...ELSE
print("a") if a > b else print("b")
