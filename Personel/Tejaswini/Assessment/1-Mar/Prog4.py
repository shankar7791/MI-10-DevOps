str1 = input("Enter a string:")
str2=""
l=len(str1)
i=l-1
while i>=0:
    str2=str2+str1[i]
    i=i-1
if str1 == str2:
    print(f"String is Palindrome i.e {str1} = {str2}")
else:
    print(f"String is not Plaidrome i.e {str1} != {str2}")