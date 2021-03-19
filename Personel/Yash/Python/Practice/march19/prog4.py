# number of occurrences of a specified element in an array

import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9,1,2,4,5,2,7,8,9,3,1,4,9,2,2,4,5])
for i in a :
    print(i,end=" ")
print()
n = int(input("Enter the element which you want to count : "))
print(f"The count of {n} is : {a.count(n)}")