#convart lower case to upper case and upper case to lower case
def check(str):
    if str.isupper()== True:
        print("convart upper case to lower case : ")
        return str.lower()
    elif str.islower() == True:
        print("convart lower case to upper case : ")
        return str.upper()
    else:
        print("invaild")      
str = input("enter the string ")
print(check(str))   