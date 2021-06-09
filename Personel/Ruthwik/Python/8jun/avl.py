# Construct AVL Algorithm and perform
    # a. Insertion
    # b. Display
    
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 
# AVL tree class which supports the
# Insert operation
class avltree():
 
    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):
     
        # Step 1 - Perform normal BST
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.height(root.left),
                           self.height(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.bal(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.r_rotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.l_rotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.l_rotate(root.left)
            return self.r_rotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.r_rotate(root.right)
            return self.l_rotate(root)
 
        return root
 
    def l_rotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.height(z.left),
                         self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                         self.height(y.right))
 
        # Return the new root
        return y
 
    def r_rotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.height(z.left),
                        self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                        self.height(y.right))
 
        # Return the new root
        return y
 
    def height(self, root):
        if not root:
            return 0
 
        return root.height
 
    def bal(self, root):
        if not root:
            return 0
 
        return self.height(root.left) - self.height(root.right)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
 
 
# Driver program to test above function
myTree = avltree()
root = None
 
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)
 
myTree.preOrder(root)
print()