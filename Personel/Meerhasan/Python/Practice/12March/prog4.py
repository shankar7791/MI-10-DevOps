
# Python set to check if string is panagram

def pangram(str): 
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet: 
		if char not in str :
			return False

	return True
	

string = input("Enter a  string : ")
if pangram(string) == True : 
	print("String is pangram : ") 
else: 
	print("Not a Pangram : ")
