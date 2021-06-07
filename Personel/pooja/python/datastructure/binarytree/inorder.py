
# Inorder = (left,root right)
# preorder = (root,left,right)
# postorder = ( left,right,root)
#         1
#        /  \
#       2     3
#      / \   /  \
#      4  5  6   7
class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def__init__(self):
        self.root = None

p = binarytree()

first = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)

p.root = first

first.left = second
first.right = third

second.left = fourth
second.right = fifth

third.left = sixth
third.right = seventh

print(first.left.left.data)