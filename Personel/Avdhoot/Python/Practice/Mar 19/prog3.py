#add and extend the array
import array as arr

num = arr.array('i', [1, 2, 3])

num.append(4)
print(num)

num.extend([5, 6, 7])
print(num)