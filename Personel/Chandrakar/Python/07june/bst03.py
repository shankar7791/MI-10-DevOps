class BST :
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self, data) :

        if self.key == data :
            return
        if self.key > data :
            if self.lchild :
                self.lchild.insert(data)
            else :
                self.lchild = BST(data)

        else :
            if self.rchild :
                self.rchild.insert(data)
            else :
                self.rchild = BST(data)

    def preoder(self):
        print(self.key,end=",")
        if self.lchild:
            self.lchild.preoder()
        if self.rchild:
            self.rchild.preoder()   
     
    
    def min_node(self) :
        current = self
        while current.lchild :
            current = current.lchild
        print("Node is minimum key is :", current.key)    

    def max_node(self) :
        current = self
        while current.rchild :
            current = current.rchild

        print("Node is max key is :", current.key)
    def search(self,data):
        if self.key == data :
            print(f"\n\n{data} is  present in tree")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else :
                print(f"\n{data} is not present in tree")
        else :
            if self.rchild :
                self.rchild.search(data)
            else :
                print(f"\n{data} is not present in tree")     
root = BST(10)
list1 = [20,4,30,4,1,5,6]
for i in list1 :
    root.insert(i)
print("preoder tree is  -  ",end=" ")
root.preoder()
while True :

    print("""
    1. node with minimum value
    2. node with maximum value
    3. Find node with given value
    4.exit
    """)
    choice = int(input("Enter the choice opration : "))
    if choice == 1 :
        root.min_node()
        print("preoder tree is  -  ",end=" ")
        root.preoder()
        continue
    if choice == 2 :
        root.max_node()
        print("preoder tree is  -  ",end=" ")
        root.preoder()
        continue
    if choice == 3 :
        data = int(input("enter the search values : "))
        root.search(data)
        print("preoder tree is  -  ",end=" ")
        root.preoder()
        continue
    else :
        print("invaild input")    
#print()
#root.min_node()
#root.max_node()