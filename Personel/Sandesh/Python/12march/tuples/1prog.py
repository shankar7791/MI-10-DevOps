# Python groupby method to remove all consecutive duplicates
from itertools import groupby 
def Remove_All_consecutive(A):
     result = [] 
     for (key,group) in groupby(A): 
          result.append(key) 

     print (''.join(result)) 

A = input("Enter String : ")
Remove_All_consecutive((A))