#leap year
def le_ap():
    year1 = int(input("enter the year : "))
    if year1 % 4 ==0:
        if year1 % 100 ==0:
            if year1 % 400 ==0:
                print(f"{year1} is leap year ")
            else:
                print(f"{year1} is  not leap year ")
        else:
            print(f"{year1} is leap year ")
    else:
        print(f"{year1} is not leap year ")                
le_ap()       
le_ap()