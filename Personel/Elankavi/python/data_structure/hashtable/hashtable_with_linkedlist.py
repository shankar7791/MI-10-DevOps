class node:
    def __init__(self,hashtable,key,value):
        self.hashtable = hashtable
        self.key = key
        self.value = value
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,newnode):
        if self.head == None:
            hash_value = l.hashing(self.key)
            self.hastable[hash_value].append(self.value)
        else:
            pass
        
    def hashing(self):
        return self.key % 10
    def display(self):
        for i in range(10):
            print(i,end = " ")
            for j in (self.hastable[i]):
                print("-----> ",end = " ")
                print(j,end=" ")
            print()

l = linkedlist()
hastable = [[] for _ in range(10)]
newnode = node(hastable,136,122)
l.insert(newnode)