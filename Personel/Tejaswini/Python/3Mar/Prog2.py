def palind(str1):
    str2=""
    l=len(str1)
    for i in str1:  
        str2 = i + str2
    if str1 == str2:
        print(f"String is Palindrome i.e {str1} = {str2}")
    else:
        print(f"String is not Plaidrome i.e {str1} != {str2}")

str1 = input("Enter a string:")
palind(str1)