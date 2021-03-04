def string(str):
    str=input("Enter the string")
    upper=0
    lower=0
    for x in str:
        if x>='A' and x<='Z':
            upper+=1
        elif x>='a' and x<='z':
            lower+=1
        else :
            pass
    print(f"count of upper case is {upper}")
    print(f"count of lower case is {lower}")
string(str)