# Python groupby method to remove all consecutive duplicates


from itertools import groupby 
def removeAllConsecutive(input): 
     
     result = [] 
     for (key,group) in groupby(input): 
          result.append(key) 
  
     print (''.join(result)) 
        
if __name__ == "__main__": 
    input = input("Enter the string: ")
    removeAllConsecutive(input)