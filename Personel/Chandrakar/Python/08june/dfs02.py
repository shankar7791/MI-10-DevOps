class node :
    def __init__(self, data =  None) :
        self.data = data 
        self.left_node = None
        self.right_node = None

class binaryTree :
    def __init__(self) :
        self.root = None
    def inorder(self) :
        if (self.root == None) :
            print("tree is Empty ...")
        else :
            self.inorder_rec(self.root)
    def inorder_rec(self, current) :   
        if current :
            self.inorder_rec(current.left_node)
            print(current.data,end=" ")
            self.inorder_rec(current.right_node)
    def preorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self.preorder_rec(self.root)
    def preorder_rec(self,current):
        if current:
            print(current.data,end=" ")
            self.preorder_rec(current.left_node)
            self.preorder_rec(current.right_node)
    def postorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self.postorder_rec(self.root)
    def postorder_rec(self,current):
        if current:
            self.postorder_rec(current.left_node)
            self.postorder_rec(current.right_node)
            print(current.data,end=" ")
                
ob1 = binaryTree()
first = node(1)                
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)
ob1.root = first
first.left_node = second
first.right_node = third
second.left_node = fourth
second.right_node = fifth
third.left_node = sixth
third.right_node = seventh
print('Inorder : ',end=" ")
ob1.inorder()
print()
print("Preorder : ",end=' ')
ob1.preorder()
print()
print("Postorder : ",end=' ')
ob1.postorder()