#program to count the number of odd and even numnber from a series of number
num= (1, 2, 3, 4, 5, 6, 7, 8, 9)    
odd = 0
even = 0
for x in num:
        if not x % 2:
    	     even += 1
        else:
    	     odd += 1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd) 

