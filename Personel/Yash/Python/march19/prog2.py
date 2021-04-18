# Program 2 : Write a Python program to find a pair with highest product from a given array of integers.Examples :
# Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
# Output: {7,8}
# Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
# Output: {-4, -6}


def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        print("No pairs exists") 
        return   

    x = arr[0] 
    y = arr[1]     
    for i in range(0, arr_len): 
        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i] 
                y = arr[j] 

    return x,y    

nums = [1] 
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = [1, 2] 
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = [1, 2, 3, 4, 7, 0, 8, 4] 
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = [0, -1, -2, -4, 5, 0, -6] 
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))
