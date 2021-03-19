# Reverse the numbers 

import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9])
print("Original String : ")

for i in a :
    print(i,end=" ")
print("\nReverse String : ")
a.reverse()
for i in a :
    print(i,end=" ")
