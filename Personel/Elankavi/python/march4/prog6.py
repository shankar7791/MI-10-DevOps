def string():
    a=input("Enter the string : ")
    b=list(reversed(a))
    if(list(a)==b):
        print("palindrome")
    else:
        print("not a palimndrome")
string()