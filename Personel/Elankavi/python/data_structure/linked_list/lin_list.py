# A simple Python program for traversal of a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
    def __init__(self):
	    self.head = None

	# This function prints contents of linked list
	# starting from head
    def printList(self):
        temp = self.head
        print("\n")
        while (temp):
            print (f"[{temp.data} | {temp.next}]------>",end=" ")
            temp = temp.next
        print("\n")

    def search(self,data):
        temp = self.head
        while (temp):
            if(temp.data == data):
                flag = 1
                if(flag == 1):
                    print("id is found")
                else:
                    print("ID is not found")    
            temp = temp.next
       
# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
    llist.printList()
    llist.search(10)