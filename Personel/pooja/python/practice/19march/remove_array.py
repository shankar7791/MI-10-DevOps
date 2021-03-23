import array as arr

num = arr.array('i', [1, 2, 3, 3, 4])
del num[2]
print(num)

del num  # whole array will get deleted
print(num)
