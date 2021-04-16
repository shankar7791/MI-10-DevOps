class pair_sum:

   def NumSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):

            if target - num in lookup:
                return (lookup[target - num], i )

            lookup[num] = i

print("Num1 = %d, Num2 = %d" % pair_sum().NumSum((10,20,10,40,50,60,70),50))
