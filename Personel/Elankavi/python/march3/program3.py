#program to check whether the string is palindrome or symmetrical
a=input("Enter the string : ")
def palindrome(a):
    b=list(reversed(a))
    if(list(a)==b):
        print("palindrome")
    else:
        print("Not a palindrome")
def symmetrical(a):
    n=len(a)
    c=0
    if(n%2):
        v=n//2+1
    else:
        v=n//2
    s1=0
    s2=v
    while(s1 < v and s2 < n):
        if(a[s1]==a[s2]):
            s2+=1
            s1+=1
        else:
            c=1
            break
    if c == 1:
        print("The string is not a symmetrical")
    else:
        print("The string is symmetrical")

        

palindrome(a)
symmetrical(a)
        