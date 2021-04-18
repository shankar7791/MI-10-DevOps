#Ceate a Function
def fibo():

# Ask for enter the number from the use  
    
    number = int(input("Enter the integer number: "))  
# Initiate value   
    first_number=0
    second_number=1
    print(first_number,second_number)
    count=2
# fibonacci series the integer number using the while loop  
    while(count<number): 
# Logic  
      third_number=  first_number+second_number
      first_number=second_number
      second_number=third_number
      print(third_number)
      count=count+1
#Calling Function
fibo()