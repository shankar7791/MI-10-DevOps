from collections import UserDict
 # inserting element in user dict 
d = {'a':1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5}
  
# Creating an UserDict
userD = UserDict(d)
print(userD.data)


# deleting element from user dict
print("Original Dictionary")
print(d)
print("**********************************") 
d.pop(1)
print(" after poping Dictionary ")