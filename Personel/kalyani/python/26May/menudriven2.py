class Node:
    def __init__(self, id, name, batch):
        self.id = id
        self.name = name
        self.batch = batch
        self.next= None


class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, newnode):
        if self.head == None:
            self.head = newnode
            self.head.next = None
        else:
            temp = self.head
            while (temp) :
                if temp.next == None:
                    temp.next = newnode
                    newnode.next=None
                temp = temp.next

    def printlist(self):
        temp = self.head
        while (temp):
            print(f"[{temp.id} {temp.name} {temp.batch}]", end="")
            temp = temp.next

    def search(self, id):
        temp = self.head
        while (temp):
            if temp.id == id :
                print('found!!!')
                print(f"[{temp.id} {temp.name} {temp.batch}]", end="")
                break
            temp = temp.next 
        else :
            print('id not found!!!')

    def delete(self, id):
        temp = self.head
        # to delete head
        if (temp is not None) and (temp.id == id):
            self.head = temp.next
            temp = None
            return
        # to delete node other than head
        while temp is not None:
            if temp.id == id:
                break
            previous = temp
            temp = temp.next

        previous.next = temp.next
        temp = None

        # print the list
        temp = self.head
        while (temp):
            print(f"[{temp.id} {temp.name} {temp.batch}]", end="")
            temp = temp.next

    def update(self, id, newName, newBatch):
        temp = self.head

        while temp != None:
            if temp.id == id:
                temp.name = newName
                temp.batch = newBatch
            
            temp = temp.next
            
        # printing the list
        temp = self.head
        while (temp):
            print(f"[{temp.id} {temp.name} {temp.batch}]", end="")
            temp = temp.next

myList = LinkedList()
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
        myList.printlist()


    elif selection == '2' :
        myList.printlist()

    elif selection == '3':
        id=int(input('enter id : '))
        myList.search(id)
    
    elif selection == '4' :
        id=int(input('enter id : '))
        myList.delete(id)

    elif selection == '5':
        id=int(input('enter id : '))
        newName=input('enter the name :')
        newBatch=input('enter the batch')
        myList.update(id, newName, newBatch)

    elif selection == '6' :
        exit()
    
    else: 
      print ("\nUnknown Option Selected!") 