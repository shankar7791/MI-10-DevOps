import UserList
  
  
L = [1, 2, 3, 4]
  
# Creating a userlist
userL = UserList(L)
print(userL.data) # printing list


# append element
L.append(5)
print("After Insertion")
print(L)

# remove method
L.remove()