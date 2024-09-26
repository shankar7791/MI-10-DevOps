# Python program to convert a list
# of character

def convert(s):

	# initialization of string to ""
	new = ""

	# traverse in the string
	for x in s:
		new += x

	# return string
	return new
	
	
# driver code
s = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(convert(s))
