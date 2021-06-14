#hash table
class HashMap:
    def __init__(self) :
        self.size = 10
        self.arr = [None]*self.size
        #print(self.bucket)

    def hashFunction(self,key):
        hash = 0
        for char in key :
            hash += ord(char)
            #print(hash)
        return hash % self.size
    def __setitem__(self, key, value) :
        h =self.hashFunction(key)
        self.arr[h] = value


h = HashMap()
#num = h.hashFunction("p")
h["a"] = 20
h["b"] = 20
h["c"] = 20
h["d"] = 20
print(h.arr)
#print(num)