#Slicing a array element
import array as arr

A = [22, 45, 53, 543, 32, 63, 24, 34]
Array= arr.array('i', A)

print(Array[2:5]) # 3rd to 5th
print(Array[:-5]) # beginning to 4th
print(Array[5:])  # 6th to end
print(Array[:])   # beginning to end