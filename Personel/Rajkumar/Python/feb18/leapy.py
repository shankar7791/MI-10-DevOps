year=int(input("Enter a year:"))
if year%400==0:
    print(f"{year} Leap Year...")
elif year%100==0:
    print(f"{year} Not Leap Year..")
elif year%4==0:
    print(f"{year} Leap Year..")
else:
    print(f"{year} Not Leap Year..")   