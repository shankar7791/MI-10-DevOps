#Convert a list of Tuples into Dictionary
def Convert(tuple, dict): 
    for a, b in tuple: 
        dict.setdefault(a, []).append(b) 
    return dict 
      
# Driver Code     
tuple = [("akash", 10), ("gaurav", 12), ("anand", 14),  
     ("suraj", 20), ("akhil", 25), ("ashish", 30)] 
dictionary = {} 
print (Convert(tuple, dictionary)) 