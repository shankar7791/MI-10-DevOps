import array as arr
array_list = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
num_array = arr.array('i', array_list)
print(num_array[2:5])
print(num_array[:-5])
print(num_array[0:-1])
print(num_array[:])
