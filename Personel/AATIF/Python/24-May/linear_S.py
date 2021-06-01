def linear_Search(list1, n, key):  

    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 15, 24, 37, 49]  
key = 15  
  
n = len(list1)  
pos = linear_Search(list1, n, key)  
if(pos == -1):  
    print("Value not found")  
else:  
    print("Value found at position: ", pos)  