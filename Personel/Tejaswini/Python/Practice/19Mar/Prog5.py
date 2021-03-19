
from array import *

arr = array('i', [1,2,3,4,5])
my_extnd_array = array('i', [7,8,9,10])
arr.extend(my_extnd_array)
print(arr)