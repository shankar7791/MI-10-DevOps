#using function
def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums [minpos] = temp
        print(nums)

nums = [15, 85,18,3,78,7]
sort(nums)
print(nums)