#  Program 5 : Remove all duplicates words from a given sentence        
# Examples:        
# Input : Geeks for Geeks Output : Geeks for        
# Input : Python is great and Java is also great Output : is also Java Python and great

rom collections import Counter 
  
def remov_duplicates(input): 
  
    input = input.split(" ") 
  
    for i in range(0, len(input)): 
        input[i] = "".join(input[i]) 
  
    UniqW = Counter(input) 
  
    s = " ".join(UniqW.keys()) 
    print (s) 
  
 
if __name__ == "__main__": 
    input = input("Enter the String: ")
    remov_duplicates(input)