# Program 4 : check given string is palindrome or not

strInput = input("Enter the string : ")

if strInput == strInput[::-1] :
  print("Entered string is a Palindrome")
else:
  print("Entered string is not a Palindrome")

# str1 = input("Enter a string:")
# str2=""
# l=len(str1)
# i=l-1
# while i>=0:
#     str2=str2+str1[i]
#     i=i-1
# if str1 == str2:
#     print(f"String is Palindrome i.e {str1} = {str2}")
# else:
#     print(f"String is not Palindrome i.e {str1} != {str2}")
