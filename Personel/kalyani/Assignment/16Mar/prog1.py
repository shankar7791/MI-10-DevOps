# python program to intechange first and last elements in a list.

list= []
n=int(input( "Enter the number of element in a list :"))
for x in Range (0, n):
    element = input( " Enter the elements :")
    list.append(elements)
    
print (" Enter your list is:" , list)    
temp = list[0]
list[0] = list[n-1]
list[n-1] = temp
print(" Enter new list is: ", list)