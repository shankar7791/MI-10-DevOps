'''
Write a Python class to find a pair of elements (indices of the two numbers) 
from a given array whose sum equals a specific target number.
Input: numbers= [10,20,10,40,50,60,70], 
target=50
Output: 3, 4
'''
class Pair:

   def sum(self, num, target):
        res = {}

        for i, num in enumerate(num):

            if target - num in res:
                return res[target - num], i 

            res[num] = i

print("Num1 = %d, Num2 = %d" % Pair().sum((10,20,10,40,50,60,70),70))