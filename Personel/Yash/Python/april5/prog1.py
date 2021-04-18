# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

print("Given array is : ")
arr = [9,8,5,2,1,4,7,8,2,3,6]
print(arr)

bubbleSort(arr)

print ("Sorted array is: ")
print(arr)