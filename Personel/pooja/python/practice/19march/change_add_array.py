import array as arr
arr_list = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr_list[0] = 0
print(arr_list)

arr_list[4:8] = arr.array('i', [1, 2, 3, 4])
print(arr_list)
