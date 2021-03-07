#Python program to calculate the sum of a list of numbers using recursion
# Algorithm :
# step 1 : Declare the list
# step 2 : Define the function lsum(n)
# step 3 : if len(n) ==1
#              return n[0]
#          else return n[0]+lsum(n[1:])
# step 4 : print and call the function   


def lsum(n):
   if len(n) == 1:
        return n[0]
   else:
        return n[0] + lsum(n[1:])

print(lsum([1,3,5,7,9]))
