
# Remove items from Set until set not become empty set

def Remove(sets) : 
	while sets : 
		sets.pop() 
		print(sets) 

sets = set([2, 4, 6, 8, 10, 12]) 
Remove(sets)
print("The End")
