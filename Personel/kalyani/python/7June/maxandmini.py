# find the node with maximum and mimimum value and find particular elements.

class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

def insert(node,key):
    if node is None:
        return Node(key)
    elif node.key < key:
        node.left = insert(node.left , key)
    else:
        node.right = insert(node.right,key)
    return node

def printree(root):
    printree(root.left)
    print(root.key,end = " ")
    printree(root.right)

def printtree(root):
    if root is not None:
        printtree(root.left)
        print(root.key,end = " ")
        printtree(root.right)

def maxvalue(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current.key

def minvalue(node):
    current = node
    while(current.right is not None):
        current = current.right
    return current.key
root = None

while(True):
    print("""
    1 -- Insert
    2 -- Maximum value
    3 -- Minimum value
    4 -- print node
    5 -- Exit
    """)
    ch = int(input("Enter the choice : "))
    
    if ch == 1:
        n = int(input("Enter no.of node : "))
        for _ in range(n):
            key = int(input("Enter the node : "))
            root = insert(root, key)
    
    elif ch == 2:
        print("The maximum node is : ",maxvalue(root))
    
    elif ch == 3:
        print("The minimum node is : ",minvalue(root))

    elif ch == 4:
        print("The traversal of the BST : ")
        printtree(root)

    elif ch == 5:
        exit()
    
    else:
        print("\nInvalid choice \n")