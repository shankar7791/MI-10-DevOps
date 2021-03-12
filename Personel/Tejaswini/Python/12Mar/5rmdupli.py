#Program using groupby method, Remove All Consicutive duplicates 

from itertools import groupby 
def rmAllCons(s):
     result = [] 
     for (key,group) in groupby(s): 
          result.append(key) 
  
     print (''.join(result)) 

s = input("Enter String : ")
rmAllCons(s) 