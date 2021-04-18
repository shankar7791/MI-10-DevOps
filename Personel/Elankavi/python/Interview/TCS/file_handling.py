#file handling

def handling():
    c=input("""
    1 - Write
    2 - Append
    3 - Read
    4 - Delete
    5 - Exit
    Enter the choice : """ )
    if(c=="1"):
        f = open("/home/kavi/MI-10-DevOps/Personel/Elankavi/python/Interview/TCS/myfile.txt","w")
        print(f.write(input("Write here : ")))
        handling()
    elif(c=="2"):
        f = open("/home/kavi/MI-10-DevOps/Personel/Elankavi/python/Interview/TCS/myfile.txt","a")
        print(f.write(input("Write here : ")))
        handling()
    elif(c=="3"):
        f = open("/home/kavi/MI-10-DevOps/Personel/Elankavi/python/Interview/TCS/myfile.txt","r")
        print(f.read())
        handling()
    elif(c=="4"):
        f = open("/home/kavi/MI-10-DevOps/Personel/Elankavi/python/Interview/TCS/myfile.txt","r")
        print(f.close())
    elif(c=="5"):
        exit()
    else:
        print("\n Enter the correct choice : ")
        handling()
   
handling()