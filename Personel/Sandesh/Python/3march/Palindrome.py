#Python program create function to check if a string is palindrome or not

def isPalindrome(A):
    return A == A[::-1]
 
A = input("Enter A String : ")
ans = isPalindrome(A)
 
if ans:
    print(f"{A}, The given string is Palindrome")
else:
    print(f"{A}, The given string is not Palindrome")