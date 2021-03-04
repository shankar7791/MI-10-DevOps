def string(str1):
    u,l=0,0

    for i in str1:
        if i>='a'and i<='z':
            l=l+1                 
        if i>='A'and i<='Z': 
            u=u+1
    print(f"Upper case Letter = {u} \nLower case Letter = {l}")

str1=input("Enter a string: ")
string(str1)