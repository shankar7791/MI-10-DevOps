#addition 

import array as arr
def addition():
    list = []
    add = 0
    n = int(input("Enter the number of element of array :-"))
    for i in range(0, n) :
        arr = int(input("Enter the element :-"))
        list.append(arr)
        add = add + list[i]
    print(f"Array is {list} ")
    print(f"Addition of  {add}")
addition()

