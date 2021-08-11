#Write a Python program to find the three largest integers from a given list of numbers using Heap queue algorithm
import heapq as hq
class heap :
    def __init__(self, list1):

        self.l = hq.nlargest(3, list1)
        print(self.l)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("orignal list is : ", list1)
obj = heap(list1)
