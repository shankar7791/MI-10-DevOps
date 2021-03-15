def em_truple(list3):
    list2= list3[0:1] +list3[2:3]+list3[3:4] 
    list1 = list2
    return list1
list1 = ([1,(),2,3])
print(f"Befor the list : {list1} ")
print("After the remove empty truple  : ",em_truple(list1))
