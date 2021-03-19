# Write a Python program to find whether a given array of integers contains any duplicate element. 
# Return true if any value appears at least twice in the said array and return false 
# if every element is distinct.

def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    if len(array_nums) == len(nums_set) :
        return False
    else :
        return True
print(test_duplicate([9,8,7,6,5,4,1]))
print(test_duplicate([1,2,3,4,4,3,2,1,5]))
print(test_duplicate([1,2,3,5,8,9,1,1,5,1,2,2,3,3,4,4,5]))