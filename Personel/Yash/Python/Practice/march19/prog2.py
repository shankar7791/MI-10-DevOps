# Access the array
import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8,9])
for i in a :
    print(i,end=" ")

print()

for i in range(len(a)) :
    print(a[i],end=" ")