y = int(input("Enter the year : "))
if(y % 4 == 0 and y % 100 != 0):
    print(y , "is a leap year")
elif(y % 100 == 0):
    print(y , "not a leap year")

elif(y % 400 == 0):
    print(y, "is a leap year")

else:
    print(y,  "not a leap year")