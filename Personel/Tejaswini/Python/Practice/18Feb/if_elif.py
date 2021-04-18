age = int(input("Enter age:"))

if age >= 13 and age <= 19 :
    print("Your are Teen") 

elif age >= 20 and age <= 40 :
    print("Your are Adult") 

elif age >60:
    print("You are Senior")

else:
    print("You are less than 13 means you are child")