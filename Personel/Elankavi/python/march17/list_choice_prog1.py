#Menu driven program on list 1)insert 2)display 3)delete 4)update 5)exit


List=list(input("Enter the number : "))
print("Your original list : ",List)
def choice():
    while True:
        ch=input("""\n
        1. Insert
        2. Display 
        3. Delete 
        4. Update
        5. Exit
        Enter your choice : """)
        if ch=='1':
            i=(input("Enter the number to insert : "))
            List.insert(-1,i)
            print("Your Modified List : ",List)
        elif ch=='2':
            for i in range(len(List)):
                print("\t",List[i],end=" ")
        elif ch=='3':
            i=input("Enter the number to delete : ")
            List.remove(i)
            print("Your Modified List : ",List)
        elif ch=='4':
            i=set(input("Enter List to update : "))
            c=set(List)
            c.update(i)
            print("your updated lis : ",list(c))
        elif ch=='5':
            print("Exit")
            exit()
        else:
            print("\nEnter the valid choice \t")
            choice()

            
choice()
