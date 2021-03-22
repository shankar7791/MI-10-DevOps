# Program 2 : Write a Python program to find a pair with highest product from a given array of integers.Examples :
# Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
# Output: {7,8}
# Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
# Output: {-4, -6}
def max(arr): 
    a_len = len(arr) 
    if (a_len < 2): 
        print("no pairs") 
        return   

    a = arr[0] 
    b = arr[1]     
    for i in range(0, a_len): 
        for j in range(i + 1, a_len): 
            if (arr[i] * arr[j] > a * b): 
                a = arr[i] 
                b = arr[j] 

    return a,b   

num1 = [1] 
print("\nOriginal array:", num1)
print("Maximum product pair is:", max(num1))           #OUTPUT:Maximum product pair is:None

num2 = [1, 2] 
print("\nOriginal array:", num2)
print("Maximum product pair is:", max(num2))          #OUTPUT:Maximum product pair is:(1,2)

num3 = [1, 2, 3, 4, 7, 0, 8, 4] 
print("\nOriginal array:", num3)
print("Maximum product pair is:", max(num3))            #OUTPUT:Maximum product pair is:(7,8)

num4 = [0, -1, -2, -4, 5, 0, -6] 
print("\nOriginal array:", num4)
print("Maximum product pair is:", max(num4))            #OUTPUT:Maximum product pair is:(-4,-6)