#Write a Python program to count the number of even and odd numbers from a series of numbers.
l = [1, 2, 4, 5, 6, 9, 11] 
  
e_count = 0
o_count = 0
num = 0     
while(num < len(l)): 
    if l[num] % 2 == 0: 
        e_count = e_count + 1
    else: 
        o_count = o_count + 1 
    num += 1
      
print("Even numbers in the list: ", e_count) 
print("Odd numbers in the list: ", o_count) 