import heapq
l = list(input("Enter the numbers : "))
print("THe 3 maximum numbers are : ")
print(heapq.nlargest(3,l))
print(heapq.heapify(l))