# create menu driven program:

# insert print search exit

class Node:
    def __init__(self,data):
        self.data= data
        self.next= None


class LinkedList:
    def __init__(self):
        self.first=None
        self.last=None

    def printList(self):
        node=self.first

        print ("\nPrinting the list...\n")
        
        while (node):
            print(node.data)
            node = node.next

    def add(self, data):
        new_node =Node(data)

        if self.first==None:     
            self.first=new_node

        if self.last !=None:
            self.last.next=new_node
        self.last= new_node

    def size(self):
        current = self.first
        count=0
        while current !=None:
            count=count+1
            current=current.next
        print ("\nSize of List is : \n", count)

    def search(self,item):
        current = self.first
        search_item=item
        found = False
        count =1
        
        while current != None and not found:
            if int(current.data) == int(search_item):
                found=True
                print ("\nSEARCH NODE FOUND AT POSITION : \n",count, " !! ")
            else:
                current=current.next
                count = count+1

        if current==None and found==False:
            print ("\nSEARCH NODE ", search_item, " NOT FOUND !! \n")


    def remove(self,search):
        current = self.first
        previous=None
        search_item=search
        found = False
        #i=0
        
        while not found:
            if current.data == search_item:
                found=True
            else:
                    previous=current
                    current=current.next
        if previous==None:
            self.last=current.next()
        else:
            previous.next=current.next
            print ("\nElement deleted\n")
        



myList = LinkedList()

menu = {}
menu['1']="Add Nodes" 
menu['2']="Search Node"
menu['3']="Delete Node"
menu['4']="Print List"
menu['5']="Exit"

while True:
    options=menu.keys()
    
    print ("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:\n")
    
    if selection =='1':
        print ("\nAdding Nodes\n") 
        
        length = int(input("Enter the number of nodes you want for your Linked List  : \n"))
        for counter in range(1,length+1) :
            item = input("\nEnter the Linked List elements : \n")
            myList.add(item)

        myList.printList()
        myList.size( )

    elif selection == '2': 
      print ("\nFinding Node\n")
      
      #Search for a node
      searchValue = input("Enter the Node value to be searched : \n ")
      myList.search(searchValue)

    elif selection == '3':
      print ("\nDeleting Node\n") 
      #Remove a Node
      delete = input("Enter the Node value to be deleted: \n ")
      myList.remove(delete)
      myList.printList()
      myList.size( )

    elif selection == '4':
        myList.printList()
        myList.size()

    elif selection == '5': 
      break

    else: 
      print ("\nUnknown Option Selected!")