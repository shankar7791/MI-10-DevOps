#>>>>>>>>>>>>>>>Array Program<<<<<<<<<<<<<<<
import array as arr  
a = arr.array('i', [2, 4, 6, 8])  
print("First element:", a[0])  
print("Second element:", a[1])  
print("last element:", a[-1])  

#>>>>>>>>>>>>change or add elements<<<<<<<<<<<<<<<<
print("\n how to change or add elements")
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
# changing first element  
numbers[0] = 0     
print(numbers)    # Output: array('i', [0, 2, 3, 5, 7, 10])  
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # Output: array('i', [0, 2, 4, 6, 8, 10]) 

#>>>>>>>>>>>>>>>delete elements from an array<<<<<<<<<<<<<<<<
print("\nDelete elements from an array")
number1 = arr.array('i', [1, 2, 3, 3, 4])  
del number1[2]                           # removing third element  
print("After deleting list: ",number1)                           # Output: array('i', [1, 2, 3, 4])  

#>>>>>>>>>>>>>>>>>Length of Array<<<<<<<<<<<<<<<
print("\nLength Of Array")
number2=arr.array('i',[1, 2, 3, 4, 5])
#Calculate a Lenght
x=len(number2)                             
print("Total Length a Array:-", x)          #Output:Total Length a Array:- 5

#>>>>>>>>>>>>>>>>Serch and get the Index<<<<<<<<<<<
print("\n Search and get the index of a value in an Array")
number3=arr.array('b',[2, 3, 4, 5, 6])
print("Index Value:- ",number3.index(3))              #Output:Index Value:- 1
