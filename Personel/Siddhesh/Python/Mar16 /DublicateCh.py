#Remove all duplicates from a given string in Python *


from collections import OrderedDict  
  

def removeDupWithoutOrder(str):  
  
    return "".join(set(str))  
  
def removeDupWithOrder(str):  
    return "".join(OrderedDict.fromkeys(str))  

if __name__ == "__main__":  
    str = "geeksforgeeks"
    print ("Without Order = ",removeDupWithoutOrder(str))  
    print ("With Order = ",removeDupWithOrder(str))  

