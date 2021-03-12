#Python groupby method to remove all consecutive duplicates
#Input  : aaaaabbbbbb
#Output : ab

from itertools import groupby 
def removeduplicates(input): 
     result = [] 
     for (key,group) in groupby(input): 
          result.append(key) 
  
     print (''.join(result)) 
input = input("enter the string : ")
removeduplicates(input)
       

