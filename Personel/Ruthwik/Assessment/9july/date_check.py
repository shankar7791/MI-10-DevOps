# Python Program to Check if a Date is Valid and Print the Incremented Date if it is.

def dc(d):
    date,mon,year = d.split('/')
    date = int(date)
    mon = int(mon)
    year = int(year)
    mon1 = [1,3,5,7,8,10,12]
    mon2 = [4,6,9,11]
    if(mon in mon1):
        m=31
    elif(mon in mon2):
        m=30
    elif(year%4==0 and year%100!=0 or year%400==0):
        m=29
    else:
        m=28
    if(mon<1 or mon>12):
        print("Date is invalid.")
    elif(date<1 or date>m):
        print("Date is invalid.")
    elif(date==m and mon!=12):
        date=1
        mon=mon+1
        print(f"The incremented date is: {date}/{mon}/{year}")
    elif(date==31 and mon==12):
        date=1
        mon=1
        year=year+1
        print(f"The incremented date is: {date}/{mon}/{year}")
    else:
        date=date+1
        print(f"The incremented date is: {date}/{mon}/{year}")


date = input('Enter date in dd/mm/yy format: \n')

dc(date)