
# Menudriven program to create delete insert update and exit in a list.

lst = []
def show_choice () :
    print('\nMenu')
    print('1 .insert ')
    print('2 .display')
    print('3 .delete')
    print('4 .update')
    print('5 . exit')
    
def_insert(l1)
i = int(input("Enter the number to insert : "))
    lst.insert(ind,insert_data)
    print(lst)
    
def_display(l1)
    print()

def_delete
i = int(input("Enter the number to delete : "))
    lst.remove(delete_data)
    print(lst)
    
def_update
i = int(input("Enter the number to update : "))
    lst.update(update_data)
    print()

def main()
    while (True) :
        choice = input('Enter choice (1-5):')
        
        if choice == '1':
            print("<<<<<<Inserting data>>>>>>")            
            insert()
        
        elif choice == '2':
            print("<<<<<<Displaying List>>>>>>")
            display()
            
        elif choice == '3 ':
            print("<<<<<<Deleting data>>>>>>")
            delete()
            
        elif choice == ' 4':
            print("<<<<<<Updating data>>>>>>")
            update()
        
        elif choice == ' 5':
            exit()
            break :
        
        else:
            print("Invalid Choice")
main()