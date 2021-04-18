#Write a Python program to calculate the sum of a list of numbers using recursion.


def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))



#Algorithm :

#step 1 : define the function and take argument.
#step 2 : check length of sum is equal to 1 then return sum of inedx 0.
#step 3 : otherwise go to else part and call the recursive method sum[0] + sum[index -1].
#step 4 : call the function and print the result.
#step-5 : STOP