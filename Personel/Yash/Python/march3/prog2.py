# Program 2 : Python program create function to check if a string is palindrome or not 

def isPalindrome(s):
    return s == s[::-1]
 
s = input("Enter the string : ")
pali = isPalindrome(s)
 
if pali:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")