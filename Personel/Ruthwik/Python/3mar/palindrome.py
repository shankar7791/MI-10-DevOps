#Program to check whether string is palindrome


str1 = input("Please enter your own String : ")
str2 = ""

for i in str1:
    str2 = i + str2  
print("String in reverse Order :  ", str2)

if(str1 == str2):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")