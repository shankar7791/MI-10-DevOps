# WAP to find three largest intergers from given from a given list of nos using heap queue algo.


import heapq
l = list(input("Enter the numbers : "))
print("THe 3 maximum numbers are : ")
print(heapq.nlargest(3,l))
print(heapq.heapify(l))