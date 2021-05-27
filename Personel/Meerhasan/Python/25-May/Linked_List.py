class Node:
    def __init__(self, id, name, batch):
       self.id = id
       self.name = name
       self.batch = batch
       self.next = None
 
class LinkedList:
    def __init__(self) :
        self.head = None
       
 
    def insert(self, NewNode):
        if self.head == None :
           self.head = NewNode
           self.head.next = None
           
        else :
            temp = self.head
            while (temp) :
                if temp.next == None :
                    temp.next = NewNode
                    NewNode.next = None 
                temp = temp.next 


    def display(self):
       temp = self.head
       print("\n")
       while(temp) :
           print(f"[{temp.id} {temp.name} {temp.batch}] ----->", end=" ")
           temp = temp.next
       print("Null\n")   

    def search(self, id) :
        temp = self.head
        while(temp) :
            if temp.id == id :
                print(f"\nStudent Id {id} Found\n")
                print(f"Student Id : {temp.id}\nStudent Name : {temp.name}\nStudent Batch : {temp.batch}")
            temp = temp.next


    def delete(self, id) :
            temp = self.head
            
            if (temp is not None) and (temp.id == id) :
                print(f"\nStudent {temp.name} Information Deleted Successfully !!")
                self.head = temp.next
                temp = None
                return
            else :
                print(f"\nStudent {id} ID Not Found !!")
                
            while temp is not None:
                if temp.id == id :
                    break
                prev = temp
                temp = temp.next

                temp.next = prev.next
                temp = None
            

    def Update(self, id, newname, newbatch) :

        temp = self.head
        while(temp) :
            if temp.id == id :
                temp.name = newmane
                temp.batch = newbatch

                print(f"\nStudent Infromaion Updated ")
                print(f"\nStudent Namme : {temp.name} \nStudent Batch : {temp.batch}")

            else :
                print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                print(f"\nStudent {id} ID Not Found")
                print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                
            temp = temp.next
            


l = LinkedList()





while True :

    print("""

1. Insert
2. Display
3. Search
4. Delete
5. Update
6. Exit
""")


    ch = int(input("Enter Your Choice => "))

    if ch == 1 :
        id = int(input("\nEnter ID : "))
        name = input("\nEnter Name : ")
        batch = input("\nEnter Batch : ")
        NewNode = Node(id, name, batch)
        l.insert(NewNode)
        

    elif ch == 2 :
        l.display()


    elif ch == 3 :
        n = int(input("\nEnter ID : "))
        l.search(n)

    elif ch == 4 :
        n = int(input("\nEnter ID : "))
        l.delete(n)

    elif ch == 5 :
        n = int(input("\nEnter ID : "))
        

        newmane = input("\nEnter New Name : ")
        newbatch = input("\nEnter New Batch : ")

        l.Update(n, newmane, newbatch)

    elif ch == 6 :
        exit()
        
    else :
        print("\nPlease Enter A Valid Input !!")

