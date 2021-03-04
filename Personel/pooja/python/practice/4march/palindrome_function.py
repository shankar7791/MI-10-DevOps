def pal_check(st):
    rev = st[:: -1]
    print("string :", st)
    print("string:", rev)
    if(st == rev):
        return True
    else:
        False


x = input("enter a string : ")
if pal_check(x):
    print("it is pallindrome")
else:
    print("not a pallindrome")
