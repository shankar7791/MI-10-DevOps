#check the string in upper case or lower case True or false 
def us(n):
    if n.isupper() == True:
        print("that number is upper case : ")
        return n.isupper()
    elif n.islower() == True:
        print("that number is lower case : ")
        return n.islower()   
        print("that is lower case")
    else:
        print("alphanumeric")    
s = input("enter the stringm : ")
print(us(s))    