# Write a Python program to calculate the sum of a list of numbers using recursion


def rls(list):
	total = 0
	for element in list :
		total = total + element

	return total
print( rls([1, 2, 3, 4, 5, 6]))
