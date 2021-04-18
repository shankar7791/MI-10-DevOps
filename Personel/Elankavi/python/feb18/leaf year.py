#program to check tthe leaf year

year = int(input("Enter the year : "))
if(year % 4 == 0 and year % 100 != 0):
    print(year , "is a leap year")
elif(year % 100 == 0):
    print(year , "not a leap year")

elif(year % 400 == 0):
    print(year, "is a leap year")

else:
    print(year,  "not a leap year")