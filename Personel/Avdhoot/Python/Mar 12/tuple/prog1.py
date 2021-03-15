#Python groupby method to remove all consecutive duplicates
#Input  : aaaaabbbbbb
#Output : ab

from itertools import groupby  

a = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3,0,0,9] 

print ("The original list is : " + str(a)) 
  
res = [i[0] for i in groupby(a)] 
print ("The list after removing consecutive duplicates : " +  str(res)) 
