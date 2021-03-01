#Check given string is palindrome or not.

ch = input("Enter a string : ")

while True :
    rev = ''.join(reversed(ch))
    print(rev, "is reverse of the string")
    if rev == ch:
        print(ch, "is palindrome")
        break
    else :
        print(ch, "is not a palindrome")
    break