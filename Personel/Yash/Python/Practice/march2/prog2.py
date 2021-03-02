#leap year
def year():
    year = int(input("Enter the year : "))
    if year % 4 == 0 and year % 100 != 0:
         print(year, "is a Leap Year")
    elif year % 100 == 0:
         print(year, "is not a Leap Year")
    elif year % 400 ==0:
         print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

year()
