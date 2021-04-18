#Print anagrams together in Python using List and Dictionary 

def Anagrams(inp): 
	
	dict = {} 
	for i in inp:  
		key = ''.join(sorted(i)) 
	
		if key in dict.keys(): 
			dict[key].append(i) 
		else: 
			dict[key] = [] 
			dict[key].append(i) 
	ana= "" 
	for key,value in dict.items(): 
		ana = ana + ' '.join(value) + ' '

	return ana 
inp = [x for x in input("Enter the list items : ").split()] 
print (Anagrams(inp)) 