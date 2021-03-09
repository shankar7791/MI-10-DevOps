#convart lower to upper and upper to lower case
def case(n):
    if n.islower()== True:
        print("convart lower case to upper case : ")
        return n.upper()
    elif n.isupper() == True:
        print("convart upper case to lower case : ")
        return n.lower()
    else:
        print("invaild")      
str = input("enter the string : ")
print(case(str))         