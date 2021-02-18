a = int(input("Enter you age : "))

if(a >= 18):
    b =input("do you have License (y/n) : ")
    if(b == "y") :
        print("You can drive now")
    else:
        print("Get an license for your vehicle then u can drive")
else:
    print("Your age is not eligible to drive")