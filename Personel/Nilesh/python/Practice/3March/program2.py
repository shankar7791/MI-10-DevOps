#Python program create function to check if a string is palindrome or not

def palindrome(s):
    if s == s[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome("aba")
palindrome("cba")
    