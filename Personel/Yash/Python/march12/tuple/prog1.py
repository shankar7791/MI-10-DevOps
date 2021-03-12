# Program 1 : Python group by method to remove all consecutive duplicatesInput  : aaaaabbbbbb
# Output : abInput : aabccba
# Output : abcba

from itertools import groupby 
def removeAllConsecutive(input): 
    result = []
    for (key,group) in groupby(input): 
        result.append(key) 
    print (''.join(result)) 

input = input("Enter the string : ")
removeAllConsecutive(input) 