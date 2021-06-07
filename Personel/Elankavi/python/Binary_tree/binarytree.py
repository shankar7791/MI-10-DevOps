class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data < data :
            if self.left == None:
                self.left = node(data)
            else:
                self.left.insert(data)
        elif self.data > data:
            if self.right == None:
                self.right = node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
    
    def printtree(self):
        if self.right:
            self.right.printtree()
        print(self.data , end = " ")
        if self.left:
            self.left.printtree()
print("-------------------------------------------------------------------------------------------------------\n")
ob = node(15)
ob.insert(3)    
ob.insert(5)
ob.insert(12)
ob.insert(33)
ob.insert(0)
ob.insert(555)
ob.printtree()
print("\n_____________________________________________________________________________________________________")
            
