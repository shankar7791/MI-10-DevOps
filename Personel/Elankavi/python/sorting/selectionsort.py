arr=[1,9,6,44,55,34,22,87,2,4,53,9,0]
def selectionsort(arr):
	l=len(arr)
	for i in range(l):
		m=i
		for j in range(i+1,l):
			if(arr[m]>arr[j]):
				m=j
			arr[m],arr[i]=arr[i],arr[m]
selectionsort((arr))
print("After sorting : ")
for i in range(len(arr)):
	print(arr[i],end=" ")
print()

