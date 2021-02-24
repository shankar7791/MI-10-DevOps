print("***Bitwise Operation***")
print("1.Binary and &")
print("2.Binary or |")
print("3.Binary xor ^")
print("4.negativ ~")
print("5.left shift <<")
print("6.Right shift >>")
selection=int(input("selection.."))

if(selection==1):
    print("your selection binary and")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a&=b
    print("Value a is:",a)
elif(selection==2):
    print("your selection binary or")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a|=b
    print("Value a is:",a)
elif(selection==3):
    print("your selection binary xor")
    a=int(input("Enter a First Number: "))
    b=int(input("Enter b Second Number: "))
    a^=b
    print("Value a is:",a)
elif(selection==4):
    print("your selection Not")
    a=int(input("Enter a First Number: "))
    b=-a
    print("Value a is:",b)
elif(selection==5):
    print("your selection Left shift)")
    a=int(input("Enter a First Number: "))
    b=a>>2
    print("Value a is:",b)
elif(selection==6):
    print("your selection Right Shift")
    a=int(input("Enter a First Number: "))
    b=a<<2
    print("Value a is:",b)
