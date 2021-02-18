
# Python program to check Leap year

year = int(input("Enter Year : "))

if year % 4 == 0 and year % 100 != 0:
    print("Is a Leap Year", year)
elif year % 100 == 0 :
    print("Is not a Leap Year", year)
elif year % 400 == 0 :
    print("I not a Leap Year", year)
else :
    print("Is not a Leap Year", year)