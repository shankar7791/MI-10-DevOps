class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insert(node,key):
	if node is None:
		return Node(key)	
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)
	return node

def printtree(root):
    if root is not None:
        printtree(root.left)
        print(root.key,end = " ")
        printtree(root.right)
    
def delete(root,key):
    if root is None:
	    return root
    if key < root.key:
	    root.left = delete(root.left, key)
    elif(key > root.key):
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValue(root.right)

        root.key = temp.key

        root.right = delete(root.right, temp.key)
    return root


def minvalue(node):
    cur = node
    while cur.left is not None:
        cur = cur.left
    return cur

def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    # Key is greater than root's key
    if root.key < key:
         search(root.right,key)
         return True
   
    # Key is smaller than root's key
    else:
        search(root.left,key)
        return(False)

# driver code 

root = None
root = insert(root , 8)
root = insert(root , 88)
root = insert(root , 98)
root = insert(root , 87)
root = insert(root , 5)
root = insert(root , 3)
root = insert(root , 58
)
print("=============================")
printtree(root)
print("\n============================")

key = int(input("Enter the node to delete : "))
print()
delete(root,key)

print("================================")
print("modified tree : ")
printtree(root)

print("\n==================================")
print("found : ", search(root,int(input("Enter the node for search : "))))