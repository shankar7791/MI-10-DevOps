# Program 1 : Write a Python program to calculate the sum of a list of numbers using recursion
'''
Algorithm :
step 1 : Declare the list
step 2 : Define the function sum(list,size)
step 3 : if size ==0
             print 0
         else list[size-1]+sum(list,size-1)
step 4 : print total and call the function   

'''
list1 = [12, 15, 25, 27, 50]
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)

total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)