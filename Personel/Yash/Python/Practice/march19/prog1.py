# import array
# x=array.array('i',[1,2,3,4,5])
# print(x)

# from array import *
# x=array('i',[1,2,3,4,5])
# print(x)

import array as arr
x= arr.array('i',[1,2,3,4,5])
print(x)

print(len(x))

x.append(6)
# x.append(1.5) #TypeError: integer argument expected, got float
print(x)

x.extend([9,8,7])
print(x)

x.insert(5, 111)
print(x)

print("Popping last ele : ",x.pop())
print("Popping 2nd ele : ",x.pop(1))
x.remove(111)
# del x[3] removing ele at ind 3
# del x del entire array
print(x)

a = arr.array('d',[1.1,2.5,3.2,5,7])
b = arr.array('d',[9.5,7.5,5.2,5,7])
c = arr.array('d')
print(a)
print(b)
print(c)
print(a+b)


print(a[1:5])
print(a[::-1])

for x in b :
    print(x)