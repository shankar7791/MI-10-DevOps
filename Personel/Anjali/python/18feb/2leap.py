year=int(input("Enter the year  "))

if year % 4 ==0 and year % 100==0 and year % 400==0 :
    print(f"{year} Year is leap year")
else :
    print(f"{year} Year is not leap year")