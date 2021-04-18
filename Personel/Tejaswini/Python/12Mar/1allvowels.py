# Python program to accept the strings which contains all the vowels
#using set

def check(str1) :

	vowels = set("aeiouAEIOU")
	s = set({})

	for char in str1 :
		if char in vowels :
			s.add(char)
		else:
			pass
			
	if len(s) == len(vowels) :
		print("Accepted")
	else :
		print("Not Accepted")

str1 = input("Enter String : ")
check(str1)