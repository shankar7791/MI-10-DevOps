# Python program to interchange first and last elements in a list
def sawp(list1):
    t = list1[0]
    list1[0] = list1[-1]
    list1[-1]=t
    return list1
list1 = [1,2,3]
print(sawp(list1))