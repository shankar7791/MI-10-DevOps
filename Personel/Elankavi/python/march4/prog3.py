#program function to accept the string and calculate the number of uppercase and lower case :
def string():
    x=input("Enter the character : ")
    u=0
    l=0
    for a in x:

        if(a>='A' and a<='Z'):
            u+=1
        elif(a>='a' and a<='z'):
            l+=1
        else:
            print("Enter the alphabetes only")

    print(f"No of Upper Case : {u} , No of lower Case : {l}")
string()

