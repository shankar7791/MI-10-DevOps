#leap year find out
a = int(input("Enter Year : "))
if a % 4 == 0 :
    print(f"{a} is leap year ")
elif a % 100 :    
    print(f"{a} is not leap year ")
elif a == 400 :
    print(f"{a} is leap year ")
else :
    print(f"{a} is  not leap year ")    
