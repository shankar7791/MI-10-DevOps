#Python program create function to check if a string is palindrome or not

string = input("Please enter your String : ")
str1 = ""

for i in string:
    str1 = i + str1

if string == str1 :
    print("The string is Palindrome")
else :
    print("The string is not Palindrome")