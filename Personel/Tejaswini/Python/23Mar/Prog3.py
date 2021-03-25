#Write a Python class to find a pair of elements (indices of the two numbers) 
#from a given array whose sum equals a specific target number. 
#Input: numbers= [10,20,10,40,50,60,70],
#target=50
#Output: 3, 4

class target_index:
   def twoSum(self, nums, target):
        lookup = {}
        
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num]+1, i+1 )
            lookup[num] = i
print("%d, %d" % target_index().twoSum((10,20,10,40,50,60,70),50))