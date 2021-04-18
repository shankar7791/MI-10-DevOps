# Prog 2 : Python program to check Leap year

year = int(input("Enter the Year : "))

if (year%400 == 0):
    print(f"{year} is a Leap Year")
elif (year%100 == 0):
    print(f"{year} is Not the Leap Year")
elif (year%4 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not the Leap Year")

'''
year = int(input("Please Enter the Year Number you wish: "))

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("%d is a Leap Year" %year)
        else:
            print("%d is Not the Leap Year" %year)
    else:
        print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
    '''