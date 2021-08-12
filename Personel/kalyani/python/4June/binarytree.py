# Implement binary tree, insert the elements and prints the tree.

class Node:
    def_init_(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class binaryTree:
    def_init_(self):
        self.root=None
        
    def__insert(self,data,ref):
        if self.root is None:
            self.root=None(data)
        else:
            new_node=Node(data)   
            if data<ref.data :
                if ref.right is not none :
                    self.insert(data,ref,right)
                else:
                    ref.right=new_node
            if data>ref.data:
                if ref.left is not none :
                    self.insert(data,ref,right)
                else:
                    ref.right=new_node
            
new_bt=binary Tree
new_bt.insert(5,new_bt.root)
new_bt.insert(4,new_bt.root)
new_bt.insert(7,new_bt.root)
new_bt.insert(12,new_bt.root)
new_bt.insert(15,new_bt.root)