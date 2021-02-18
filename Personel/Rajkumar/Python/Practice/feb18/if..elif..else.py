a=int(input("Enter a Number:"))
if a%400==0:
    print(f"{a} Leap Year...")
elif a%100==0:
    print(f"{a} Not Leap Year..")
elif a%4==0:
    print(f"{a} Leap Year..")
else:
    print(f"{a} Not Leap Year..")        