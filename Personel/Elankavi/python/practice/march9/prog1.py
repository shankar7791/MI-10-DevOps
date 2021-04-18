#modifying string

def string():
    a=input("Enter the character : ")
    b=int(input(""" choose the option : 
    1.upper case
    2.lower case
    3.strip
    4.replace  :  """))
    if(b==1):
        print(f"The upper case of the {a} is : ",a.upper())
    elif(b==2):
        print(f"The lower case of the {b} is : ",a.lower())
    elif(b==3):
        print(f"The Ans is : ",a.strip())
    elif(b==4):
        c=input("Enter the replace character : ")
        print(f"The replacing of {a} is : ",a.replace(a,c))
string()
    