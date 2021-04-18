#check string is in lower case or in upper case
def string(str1):
    if str1.isupper():
        print("the string is in upper case : ")
        return str1.isupper() 
    elif str1.islower():
        print("the string is in lower case")
        return str1.islower()   
    else:
        print("string is alphanumeric")    
s = input("enter the string : ")
print(string(s))    