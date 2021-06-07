'''[ID,Name,Batch]'''
class Node:
    def __init__(self,id,name,batch):
        self.id=id
        self.name=name
        self.batch=batch
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head == None :
            self.head == newNode
            self.head.next= None
        else:
            temp =self.head
            while(temp):
                temp.next = newNode
                newNode.next = None
                temp = temp.next

    def printList(self) : 
        temp=self.head
        print("\n")
        while(temp):
            print(f"[{temp.id}{temp.name}{temp.batch}]---->",end="") 
            temp = temp.next
        print("Null\n")             
    def search(self,id):
        emp=self.head
            print("\n")
            while(temp):
                if temp.id == id: 
                    print(f"\n student id{id} Found")
                    print(f"[student Id:{temp.id}\n student nane:{temp.name}\n student batch:{temp.batch}]--->",end="")
                    break
                temp = temp.next
            else:
                print(f"\n student id{id} Found")

llist = LinkedList()
while(True):
    print('''
    1.insert
    2.Display
    3.search
    4.Exit''')

ch = int(input("Enter the your choice!!!"))

if ch==1:
    id = int(input("Enter the student ID :"))
    name=input("enter student name:")
    batch = input("Enter student Batch :")
    newNode = Node(id,name,batch)
    llist.insert(newNode)

if ch == 2:
    llist.printList()
elif ch = 3:
    id = int(input(Enter student id))
if ch ==4:
    exit()