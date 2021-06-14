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
    def inorder(self) :
        if self.lchild :
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild :
            self.rchild.inorder()    

    def postorder(self) :
        if self.lchild :
            self.lchild.postorder()
        if self.rchild :
            self.rchild.postorder()
        print(self.key,end=" ")  

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
    def delete(self,data) :
        if self.key is None :
            print("tree is empty !")
            return
        if data < self.key :
            if self.lchild :
                self.lchild = self.lchild.delete(data)
            else :
                print("Given node is not present in tree ")
        elif data >self.key :
            if self.rchild :
                self.rchild = self.rchild.delete(data)
            else :
                print("Given node is not present in tree ")
        else :
            if self.lchild is None :
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None :
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild :
                node = node.lchild

            self.key = node.key
            self.rchild =self.rchild.delete(node.key)
        return self        
    



root = BST(10)
list1 = [20,4,30,4,1,5,6]
for i in list1 :
    root.insert(i)
print("preoder tree is  -  ",end=" ")
root.preoder()

root.search(4)

print("inorder tree is  -  ",end=" ")
root.inorder()

print("\npostorder  tree is - ",end=" ")
root.postorder()

n = 10
root.delete(n)
print("\ndelete the node -",n)
print("\nAfter the deleting - ",end=" ")
root.preoder()