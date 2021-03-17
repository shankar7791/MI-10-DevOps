# Menudriven Program on List 1.insert 2.Display 3.update 4.delete 5.Exit

lst = []

def create() :
    n = int(input(("Enter how many elements required in List : ")))   
    for i in range(n) :
        ele = input()
        lst.append(ele)
    print(lst)

def display() :
    print(lst)

def insert() :
    ind = int(input("At what index do you want to insert : "))
    insert_data = input("Enter the data to insert : ")
    lst.insert(ind,insert_data)
    print(lst)

def update() :
    up = int(input("At what index do you want to update value : "))
    update_data = input("Enter the data to update : ")
    lst[up] = update_data
    print(lst)

def delete() :
    delete_data = input("Enter the data to delete : ")
    lst.remove(delete_data)
    print(lst)

while True :
    print("""   
    ****____Menudriven Program on List____****
    1.Create 
    2.Display
    3.Insert data
    4.Update data 
    5.Delete data
    6.Exit
""")
    choice = input("Enter the choice : ")
    if choice in ('1', '2', '3', '4', '5', '6') :
        if choice == '1' :
            print("<<<<<<Creating List>>>>>>")
            create()
        if choice == '2' :
            print("<<<<<<Displaying List>>>>>>")
            display()
        if choice == '3' :
            print("<<<<<<Inserting data>>>>>>")            
            insert()
        if choice == '4' :
            print("<<<<<<Updating data>>>>>>")
            update()
        if choice == '5' :
            print("<<<<<<Deleting data>>>>>>")
            delete()
        if choice == '6' :
            print("Do you really want to exit (y/n) : ",end="")
            ex = input("")
            if ex == 'y' :
                exit()
    else :
        print("Invalid Choice")

