arr=[55,4,9,8,0,32,34,12,65]
def insertionsort(arr):
	l=len(arr)
	for i in range(1,l):
		a=arr[i]
		j=i-1
		while(j>=0 and a<arr[j]):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=a
print("Insertion sort")
insertionsort(arr)
for i in range(len(arr)):
	print(arr[i],end=" ")
print()