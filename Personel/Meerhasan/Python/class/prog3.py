
# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number

class pair :
   def twoSum(self, nums, target) :
        lookup = {}

        for i, num in enumerate(nums) :

            if target - num in lookup :
                return (lookup[target - num], i )

            lookup[num] = i
print(" index-1 = %d \n index-2 = %d" % pair().twoSum((10,20,10,40,50,60,70),50))

