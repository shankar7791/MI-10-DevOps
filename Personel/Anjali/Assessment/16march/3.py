#Check if a Substring is Present in a Given String
def present():
    str1=input("Enter the string  ")
    str2=input("Enter the string for search  ")
    print(str1.find(str2))
    if (str1.find(str2))==-1):
        print("not present")
    else:
        print(" present")
present()