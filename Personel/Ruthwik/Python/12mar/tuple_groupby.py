# Python groupby method to remove all consecutive duplicates

from itertools import groupby 
def tgb(i): 

     result = [] 
     for (key,group) in groupby(i): 
          result.append(key) 
  
     print (''.join(result)) 

i = tuple(input('Enter a tuple : '))
print(i)
tgb(i) 