# Program 3 : Write a Python class to find a pair of elements (indices of the two numbers) 
# from a given array whose sum equals a specific target number. 
# Input: numbers= [10,20,10,40,50,60,70],
# target=50
# Output: 2,3

class Solution :
    def __init__(self,arr,sum):
        print("Welcome")
        self.arr = arr
        self.sum = sum
    def getArray(self) :
        print(self.arr)
    def findPair(self) :
        for i in range(0, len(self.arr)):
            for j in range(i + 1, len(self.arr)):
                if self.arr[i] + self.arr[j] == self.sum:
                    return i ,j

sl = Solution([10,20,10,40,50,60,70],50)
sl.getArray()
print(sl.findPair())