#

def checkpalindrome(str):
    i = 0
    j = len(str) - 1
    while i <= j:
        if (str[i] != str[j]):
            return False
        i += 1
        j -= 1
    return True


str = input("enter the string :")
result = checkpalindrome(str)
if result == True:
    print("the given string is a pallindrome")
else:
    print("the given string is not a pallindrome")
