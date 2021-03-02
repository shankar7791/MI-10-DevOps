#Ceate a Function
def fact():

# Ask for enter the number from the use  
    
    number = int(input("Enter the integer number: "))  
# Initiate value   
    fact_number=1
# factorial the integer number using the for loop  
    for i in range(1, number+ 1): 
# Logic  
      fact_number = fact_number* i
  
# Display the result  
    print("factorial of ", number, " is ", fact_number)
#Calling Function
fact()