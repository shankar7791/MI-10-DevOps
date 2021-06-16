class node:
    def __init__(self,id,name,batch):
        self.id = id
        self.name = name
        self.batch = batch
        self.next = None
class linked_list:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while(temp):
                if temp.next == None:

                    temp.next = newnode
                    newnode.next = None
                temp = temp.next

    def display(self):
        temp = self.head
        while(temp):
            print(f"ID : {temp.id} , Name : {temp.name} , Batch : {temp.batch} ---> ",end=" ")
            temp = temp.next
        print("null")
    def update(self,newnode):
        temp = self.head
        while(temp):
            if temp.id == newnode.id:
                temp.name = newnode.name
                temp.batch = newnode.batch
            else:
                print("id not found")
            temp = temp.next
        print("Your node : ")
        ob.display()

    def search(self,id):
        temp = self.head
        while(temp):
            if temp.id ==id:
                print(f" Name : {temp.name}  Batch : {temp.batch} " )
                break
            temp = temp.next
        else:
            print("ID not found")

    def delete(self,id):
        temp = self.head 
        if (temp is not None) and (temp.id == id):
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            if temp.id == id:
                break
            previous = temp
            temp = temp.next

        previous.nsext = temp.next
       
    



ob = linked_list()

# driver code
while(True):
    print("""
    1 - Insert
    2 - Display
    3 - Update
    4 - Search
    5 - Delete
    6 - exit
    """)
    ch = int(input("Enter the choice : "))
    if ch == 1:
        id = int(input("Enter the id : "))
        name = input("Enter the name : ")
        batch = input("Enter the Batch name / No : ")
        newnode=node(id,name,batch)
        ob.insert(newnode)
    
    elif ch == 2:
        ob.display()

    elif ch == 3:
        id = int(input("Enter  your id : "))
        name = input("Enter the New name : ")
        batch = input("Enter your NEw Batch name / no : ")
        newnode = node(id,name,batch)
        ob.update(newnode)


    elif ch == 4 :
        id = int(input("Enter your id : "))

        ob.search(id)

    elif ch == 5:
        id = int(input("Enter your id : "))

        ob.delete(id)
    
    elif ch == 6:
        exit()
    
    else:
        print(" Invalid choice ")