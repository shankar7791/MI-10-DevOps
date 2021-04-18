#Convert List to Tuple

def convert(list): 
    return tuple(list) 
li = [x for x in input("Enter List of Item: ").split()]
print("List Input : ",li)
print("Output : ",convert(li)) 