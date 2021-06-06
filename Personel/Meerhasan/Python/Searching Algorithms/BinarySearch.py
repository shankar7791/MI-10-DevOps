
from bisect import bisect_left

def BinarySearch(a_list, value):
	i = bisect_left(a_list, value)
	if i != len(a_list) and a_list[i] == value:
		return i
	else:
		return -1

a_list = [1, 2, 4, 4, 8]
value = int(input("Enter Number To Search : "))
ob = BinarySearch(a_list, value)
if ob == -1:
	print(f"{value} Not Found !!")
else:
	print(f"{value} Is Present At Index {ob}")
