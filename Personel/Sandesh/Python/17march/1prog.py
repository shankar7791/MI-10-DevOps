
while True : 
    List = [10,20,30,40]
    print("List - ",List)
    print("user can perform following operation from above list")
    print("""
    1. insert
    2. delete
    3. Display
    4. Update
    5. Exit
    """)
    
    ch = int(input("Enter the number : "))
    if ch == 1 :
        Lis = int(input("At what index do you want to insert : "))
        List1 = int(input("Enter a number which you want to insert on list : "))
        List.insert(Lis,List1)
        print("After inserting a number in list",List)

    elif ch == 2 :
        List1 = int(input("Enter a number from a list, which you wanna delete : "))
        List.remove(List1)
        print("After a removing number from list", List)

    elif ch == 3 : 
        print("List", List)

    elif ch == 4 : 
        List1 = int(input("At what index do you want to update value : " ))
        update_list = int(input("Enter a data to update :"))
        List[List1] = update_list
        print("After a updating or replacing a number in list",List)

    elif ch == 5 : 
        print("Thank You !!! ")
        exit()
    else : 
        print("Invalid input from user")
        continue
