#menu driven python program in list
 


#list = [x for x in input("Enter the List :-").split()]
list = []
def create() :
    num = int(input("Enter the element in the list :-"))
    for i in range(0, num) :
        element = int(input("Enter the element :-"))
        list.append(element)
    print(list)

def insert() :
    index = int(input("When the index at which element is inserted :-"))
    element = input("Enter the insert element ;-")
    list.insert(index , element)
    print(list)


def display() :
    print(f"List Display", list)


def update() :
    index = int(input("When the index at which element is updated :-"))
    element = input("Enter the updated element :-")
    list[index] = element
    print(list)

def delete() :
    element = int(input("Enter the delete element :-"))
    list.remove(element)
    print(list)

while True :
    print("""  ***  MENU DRIVEN PROGRAM ***
           1. Create
           2. Insert
           3. Display
           4. Update
           5. Delete 
           6. Exit """)
    choice = int(input("Enter Your Choice :-"))

    if choice == 1 :
        print("Create List :-")
        create()
    elif choice == 2 :
        print("Insert Element :-")
        insert()
    elif choice == 3 :
        print("Display List :-")
        display()
    elif choice == 4 :
        print("Updated List :-")
        update()
    elif choice == 5 :
        print("Delete Element :-")
        delete()
    elif choice == 6 :
        print("Exit")
        exit()
    else :
        print("Please enter valid choice !!")


