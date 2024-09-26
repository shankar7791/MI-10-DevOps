# function to remove all consecutive duplicates
# from the string in Python

from itertools import groupby
def removeAllConsecutive(input):
	

	result = []
	for (key,group) in groupby(input):
		result.append(key)

	print (''.join(result))
	
# Driver program
if __name__ == "__main__":
	input = 'aaaaabbbbbb'
	removeAllConsecutive(input)
