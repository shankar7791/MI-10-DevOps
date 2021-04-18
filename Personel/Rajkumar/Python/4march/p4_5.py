# Write a Python program function to print the even numbers from a given list.
#create a function
def even(list1):  
#  each number in list 
    for num in list1: 
      
    # checking condition 
        if num % 2 == 0: 
          print(num, end = " ") 
# list of numbers 
list1 = [1,2,6,10,95,7,31,21,22]
#calling function
even(list1)
