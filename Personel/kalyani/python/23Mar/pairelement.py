# Write a python class to find a pair of elements from a given array whose sum equals a specific target number .

class Pair:
    
   def sum(self, num, target):
        res = {}

        for i, num in enumerate(num):

            if target - num in res:
                return res[target - num], i 

            res[num] = i

print("Num1 = %d, Num2 = %d" % Pair().sum((10,20,10,40,50,60,70),70)) 