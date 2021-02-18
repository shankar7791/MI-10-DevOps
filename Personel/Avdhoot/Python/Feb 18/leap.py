y = int(input("Enter a year "))

if y % 4 == 0 :
    if y % 100 == 0 :
        if y % 400 == 0 :
            print("Year is Leap year")
        else :
            print("Year is not Leap year")
    else :
        print("Year is leap year")
else:
    print("Year is not Leap year")

                

