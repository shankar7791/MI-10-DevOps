list1 = [1, 3, 4, 6, 8]
list2 = [4, 5, 6, 2, 10]
  
print ("list 1 : ",list1)
print ("list 2 : ",list2)
res_list = []
for i in range(0, len(list1)):
    res_list.append(list1[i] + list2[i])
  
print ("Adiition of list is : ",res_list)