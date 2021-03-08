#Write a Python program to calculate the sum of a list of numbers using recursion.

#algorithm
#step 1 : define the function and take argument.
#step 2 : check length of sum is equal to 1 then return sum of inedx 0.
#step 3 : otherwise go to else part and call the recursive method sum[0] + sum[index -1].
#step 4 : call the function and print the result.
#step-5 : STOP

# list = [1,3,5]
# call recursive method: 
# first iteration : i = 1     sum = 0 + 1 = 0   now sum = 1
# second iteration : i = 3    sum = 1 + 3 = 4   now sum = 4
# last iteration : i = 5      sum = 4 + 5 = 9   final output  sum = 9    

def listsum(sum):
   if len(sum) == 1:
        return sum[0]
   else:
        return sum[0] + listsum(sum[1:])

print(listsum([1,3,5,7,9]))