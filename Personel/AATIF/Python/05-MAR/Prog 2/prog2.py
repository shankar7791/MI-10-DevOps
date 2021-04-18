# Write a Python program to calculate the sum of a list of numbers using recursion.

# define a function passing parameter
# Initialize a variable t = 0
# Using for loop take a inherit varialbe e for a parameter passed
# Using If statement apply condition type(e) == type([])
# Apply the method to variable t = t + list_sum(e)
# Apply else condition when the If condition get false t = t + e
# return t
# print by calling function using arguments
 
def list_sum(data_list):
	t = 0
	for e in data_list:
		if type(e) == type([]):
			t = t + list_sum(e)
		else:
			t = t + e

	return t
print(list_sum([1, 2, [3,4],[5,6]]))