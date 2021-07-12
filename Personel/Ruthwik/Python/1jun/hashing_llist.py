class Node(object):
    def __init__(self, key):
        self.key = key 
        self.next = None 
        self.pre = None 
    
    def __repr__(self):
        value = '{%d}' % (self.key)
        return value

class HashTable(object):
    '''
    Implementation of hash table (link method)
    '''
    def __init__(self, T = []):
        self.T = T #Hashlist
        self.m = len(self.T) #Hash table capacity (number of slots) 
        self.size = 0 #Number of all elements in the hash table
    
    def _hash(self, key):
        #Define hash function
        return abs(key) % self.m
    
    def insert(self, node):
        #Insert a node
        k = self._hash(node.key) #Hash value
        if self.T[k] == None: #There is no value in this linked list
            self.T[k] = node 
            node.next = None 
            node.pre = None 
        else:
            node.next = self.T[k] #There are values ​​in this linked list
            self.T[k].pre = node 
            self.T[k] = node 
            self.T[k].pre = None 
        self.size += 1
    
    def search(self, key): #Search by keyword
        k = self._hash(key)
        current = self.T[k]
        while current != None and current.key != key:
            current = current.next 
        if current == None : #When not found
            return "keyerror"
        return True 

    def delete(self, node): #Delete the specified node of the hash table
        k = self._hash(node.key)
        if node == self.T[k]:
            self.T[k] == None 
        elif node.next == None:
            node.pre.next = None 
        else:
            node.next.pre = node.pre 
            node.pre.next = node.next 
        self.size -= 1
        return node 

    def printlist(self): #Visualization hash table
        res = [None for _ in range(self.m)]
        for i in range(self.m):
            k = self.T[i]
            line = ''
            while k:
                line += '%s' %k
                k = k.next
                if k:
                    line += '<=>'
            res[i] = line 
        print(res)

if __name__=='__main__':
    T = HashTable([None for _ in range(10)])
    nodes = []
    for i in range(31):
        node = Node(i)
        nodes.append(node)
    
    menu = {}
    menu['1']="Add Nodes" 
    menu['2']="Print List"
    menu['3']="Search Node"
    menu['4']="Delete Node"
    menu['5']="Update Node"
    menu['6']="Exit"

    while True:
        options=menu.keys()
        
        print ("\nMENU")
        print("======================\n")
        for entry in options: 
            print(entry, menu[entry])
        print("")
        selection = input("\nPlease Select:\n")

        if selection == '1' :
            print ("\nAdding Nodes\n") 
            length = int(input("Enter the number of nodes you want for your Linked List  : \n"))
            for counter in range(1,length+1) :
                item = int(input("\nEnter the elements : \n"))
                
                T.insert(nodes[item])
            f = open("School_M.txt", "w")
            f.writelines("\r\nStudent ID: "+ str(T) +" \r\n")
            f.close()
            T.printlist()


        elif selection == '2' :
            T.printlist()

        elif selection == '3':
            id=int(input('enter id : '))
            T.search(id)
        
        elif selection == '4' :
            id=int(input('enter id : '))
            T.delete(id)

        elif selection == '5':
            id=int(input('enter id : '))
            newName=input('enter the name :')
            newBatch=input('enter the batch')
            T.update(id, newName, newBatch)

        elif selection == '6' :
            exit()
        
        else: 
            print ("\nUnknown Option Selected!") 


