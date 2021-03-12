
# Program to accept the strings which contains all vowels



def check(string) :

	vowels = set("aeiou")

	s = set({})

	for x in string :

		if x in vowels :
			s.add(x)
		
	if s == vowels :
		print("Accepted")
	else :
		print("Not Accepted")
	
string = input("Enter a string : ")

	
check(string)
