class Node :
    def __init__(self, id, name, batch) : 
        self.id = id
        self.name = name
        self.batch = batch
        self.next = None
        self.prev = None

class Doublylist:
    def __init__(self):  
        self.head = None

    def insert(self, newNode) :
        if(self.head is not None) :
            current = self.head
            while(current.next is not None) :
                current = current.next
            current.next = newNode
            newNode.prev = current
        else:
            self.head = newNode

    def print_list(self) :
        temp = self.head

        while(temp) :
            print(f"[{temp.id},{temp.name},{temp.batch}]<--->",end="")
            temp = temp.next
        print("[NULL]")

    def search_list(self, id) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                print(f"\nStudent ID Found")
                print(f"\nStudent ID : {temp.id} \nStudent Name : {temp.name} \nStudent Batch : {temp.batch}")
                break
            temp = temp.next
        else :
            print("\nStudent ID not Found")

    def update_list(self, id, new_name, new_batch) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                temp.name = new_name
                temp.batch = new_batch
                break
            temp = temp.next
        else :
            print("\nStudent ID not found for update")

    def delete_list(self, id) :
        
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head.next is None:
            if self.head.id == id:
                self.head = None
            else:
                print("Item not found")
            return 

        if self.head.id == id:
            self.head = self.head.next
            self.head.prev = None
            return
        
        temp = self.head
        while temp.next is not None:
            if temp.id == id:
                break
            temp = temp.next
        
        if temp.next is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        else:
            if temp.id == id:
                temp.prev.next = None
            else:
                print('element not found')


    
myList = Doublylist()
menu = {}
menu['1']="Add Nodes" 
menu['2']="Print List"
menu['3']="Search Node"
menu['4']="Delete Node"
menu['5']="Update Node"
menu['6']="Exit"

while True:
    options=menu.keys()
    
    print ("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:\n")

    if selection == '1' :
        print ("\nAdding Nodes\n") 
        length = int(input("Enter the number of nodes you want for your Linked List  : \n"))
        for counter in range(1,length+1) :
            # item = input("\nEnter the Linked List elements : \n")

            id=int(input('enter id : '))
            name=input('enter the name :')
            batch=input('enter the batch')
            newnode= Node(id,name,batch)
            myList.insert(newnode)
        myList.print_list()


    elif selection == '2' :
        myList.print_list()

    elif selection == '3':
        id=int(input('enter id : '))
        myList.search_list(id)
    
    elif selection == '4' :
        id=int(input('enter id : '))
        myList.delete_list(id)
        myList.print_list()

    elif selection == '5':
        id=int(input('enter id : '))
        newName=input('enter the name :')
        newBatch=input('enter the batch')
        myList.update_list(id, newName, newBatch)

    elif selection == '6' :
        exit()
    
    else: 
      print ("\nUnknown Option Selected!") 

