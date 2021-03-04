# Write a Python function to sum all the numbers in a list.
#declare a Function
def sum(list):
#Initialize a variable
    t= 0
# Iterate each element in list,and add them in variale total
    for i in range(0, len(list)):
      t = t + list[i]
 
# printing total value
    print("Sum of all elements in given list: ", t)
# creating a list
list= [11, 5, 17, 18, 23] 
#calling Function
sum(list)