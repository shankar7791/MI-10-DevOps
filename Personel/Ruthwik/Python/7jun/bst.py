class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
 
    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key < node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
 
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
 
    def replace_node_of_parent(self, new_node):
        if self.parent is not None:
            if new_node is not None:
                new_node.parent = self.parent
            if self.parent.left == self:
                self.parent.left = new_node
            elif self.parent.right == self:
                self.parent.right = new_node
        else:
            self.key = new_node.key
            self.left = new_node.left
            self.right = new_node.right
            if new_node.left is not None:
                new_node.left.parent = self
            if new_node.right is not None:
                new_node.right.parent = self
 
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
 
    def remove(self):
        if (self.left is not None and self.right is not None):
            successor = self.right.find_min()
            self.key = successor.key
            successor.remove()
        elif self.left is not None:
            self.replace_node_of_parent(self.left)
        elif self.right is not None:
            self.replace_node_of_parent(self.right)
        else:
            self.replace_node_of_parent(None)
 
    def search(self, key):
        if self.key > key:
            if self.left is not None:
                return self.left.search(key)
            else:
                return None
        elif self.key < key:
            if self.right is not None:
                return self.right.search(key)
            else:
                return None
        return self
 
 
class BSTree:
    def __init__(self):
        self.root = None
 
    def inorder(self):
        if self.root is not None:
            self.root.inorder()
 
    def add(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
 
    def remove(self, key):
        to_remove = self.search(key)
        if (self.root == to_remove
            and self.root.left is None and self.root.right is None):
            self.root = None
        else:
            to_remove.remove()
 
    def search(self, key):
        if self.root is not None:
            return self.root.search(key)
 
bst=BSTree()
menu = {}
menu['1']="Add Data" 
menu['2']="Delete Data"
menu['3']="Search"
menu['4']="Print Data"
menu['5']="Exit"

while True:
    options=menu.keys()
    
    print ("\nMENU")
    print("======================\n")
    for entry in options: 
      print (entry, menu[entry])
    print("")
    selection = input("\nPlease Select:\n")

    if selection == '1' :
        print ("\nAdding Data\n") 
        length = int(input("Enter the number of data you want for your Hash Table : \n"))
        for counter in range(1,length+1) :
    
            value=int(input('enter the value :'))
            bst.add(value)


    elif selection == '2' :
        value = int(input('enter the value :'))
        bst.remove(value)

    elif selection == '3':
       value = int(input('enter the value :'))
       bst.search(value)
    
    elif selection == '4':
        bst.inorder()
        print()

    elif selection == '5':
        exit()

    else: 
      print ("\nUnknown Option Selected!") 