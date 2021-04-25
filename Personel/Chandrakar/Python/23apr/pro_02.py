d = {101 : "aatif",102 : "avdhoot",103 : "anjali",104 : "chandrakar",105 : "meerhasan"}

while True :

    print("""
        1.Add student
        2.Show
        3.Delet
        4.Update
        5.Search
        6.Exit""")


    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        roll_n = int(input("Enter the new student roll number  = "))
        name_n = input("Enter the new student name = ")
        d[roll_n]=name_n
        print(d)
    elif ch == 2 :

        print(d)   
    elif ch == 3:
        rol = int(input("Enter the roll number : "))
        d.pop(rol)    
        print(d)
    elif ch == 4 :
        while (True):
            print("""Choice the updation :
            1.Student Name  update
            2.Roll Number  update3
            3.exit
            """) 
            ch1 = int(input("Enter the choice  : "))

            if ch1 == 1:
                up_r =int(input("Enter the student roll number : "))
                up_n =input("Enter the student update name : ")
                
                d[up_r]=up_n
                print(d)

            elif ch1 == 2:
                o_rol = int(input("Enter old roll number : "))
                d.pop(o_rol)
                print(d)
                up_r =input("Enter the student name  : ")
                up_n =int(input("Enter the new roll number : "))
                d[up_n]=up_r
                print(d)
            elif ch1 == 3:
                print("Exit")
                break    

            else :
                print("Invaild choise")

    elif ch == 5:
        print("""Search option :
            1.Search name
            2.Exit """)
        while True :
            ch = int(input("Enter the choise : "))

            if ch == 1:
                
                rol = int(input("Enter the roll number : "))
                search =  d.get(rol)   
                print("Search name is : ",search) 
            elif ch == 2 :
                print("Exit")
                break
            else :
                print("Invaild choise Try again")


    elif:
        print("exit") 
        break
    else :
        print("Invaild choise  ")   
