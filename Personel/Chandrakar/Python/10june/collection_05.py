# Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm.
import heapq as hq
class heap :
    def __init__(self, list1):
        self.list1 = list1            
        self.l = hq.heapify(self.list1)
        print("heapify is  : ",self.list1)
list1 = [25, 44, 68, 21, 39, 23, 89]
print("raw heap is : ", list1)
obj = heap(list1)