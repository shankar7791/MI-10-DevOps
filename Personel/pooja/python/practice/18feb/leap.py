 # Prog 2 : Python program to check Leap year
 
 year = 2000
 
 #year = int(input("enter the year :"))
  

if(year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) == 0:
          print("{0} is a leap year ".format(year))
        else:
         print("{0} is not a leap year : ".format(year))
    else :
        print("{0} is a leap year ".format(year))
        
else :
    print("{0} is not a leap year".format(year))