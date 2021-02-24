#Python program to count the number of even and odd numbers from a series of numbers.
 
n1 = int(input("Enter the starting number")) 
n2 = int(input("Enter the starting number")) 

even_count, odd_count = 0, 0
       
while(n1 < n2): 
      
    # checking condition 
    if n1 % 2 == 0: 
        even_count += 1
    else: 
        odd_count += 1
      
    # increment num  
    n1 += 1
      
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 