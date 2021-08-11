# Write a Python program to delete the smallest element from the given Heap and then inserts a new item. (edited) 
import heapq as hq
class heap :
    def __init__(self, list1):
        self.list1 = list1            
        self.l = hq.heapify(self.list1)
        print("heapify is  : ",self.list1)
    def new_item(self) :
        hq.heapreplace(self.list1, 21)
        print("replace : ", self.list1)
        hq.heapreplace(self.list1, 110)   
        print("Ater replace : ", self.list1) 
list1 = [25, 44, 68, 21, 39, 23, 89]
print("raw heap is : ", list1)
obj = heap(list1)
obj.new_item()