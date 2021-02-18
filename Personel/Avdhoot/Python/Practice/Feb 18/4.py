#if...elif...else

a = int(input("Enter First Number "))
b = int(input("Enter Second Number "))
c = int(input("Enter Third Number "))

if a > b :
    print(f"{a} is Greater")

elif b > c :
    print(f"{b} is Greater")
    
else :
    print(f"{c} is Greater")