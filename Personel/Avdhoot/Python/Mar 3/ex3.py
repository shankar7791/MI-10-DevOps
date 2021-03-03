#Python program to check whether the string is Symmetrical or Palindrome

string = input("Please enter your String : ")
str1 = ""

for i in string:
    str1 = i + str1  

if string == str1 :
    a = len(str1)
    b = a % 2
    if b == 0 :
        print("String is symmetrical and Palindrome")

else :
    print("String is not symmetrical and Palindrome")

