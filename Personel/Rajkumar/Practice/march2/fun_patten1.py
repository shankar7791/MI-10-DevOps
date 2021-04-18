#Ceate a Function
def patten1():

# Ask for enter the number from the use  
    
    number = int(input("Enter the integer number: "))  
    for i in range(0, number):
     
        # inner loop to handle number of columns
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
#Calling Function
patten1()