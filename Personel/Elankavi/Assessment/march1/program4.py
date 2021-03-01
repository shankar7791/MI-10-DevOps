s=input("Enter the string : ")
r=list(reversed(s))
s2=list(s)
if(s2==r):
    print("palindrome")
else:
    print("not a palindrome")