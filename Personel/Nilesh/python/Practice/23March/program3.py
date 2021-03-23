#Program 3 : Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#Input: numbers= [10,20,10,40,50,60,70],
#target=50
#Output: 3, 4

class number:
   def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return (dict[target - num], i )
            dict[num] = i
print("index1=%d, index2=%d" % number().twoSum((10,20,10,40,50,60,70),50))