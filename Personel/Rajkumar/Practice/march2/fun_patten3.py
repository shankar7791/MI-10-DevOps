#Ceate a Function
def patten3():

# Ask for enter the number from the use  
    
    number = int(input("Enter the integer number: "))  
    for i in range(0, number):
     
        # inner loop to handle number of columns
        for j in range(1, i+1):
         
            # printing stars
            print(j,end="")
      
        # ending line after each row
        print("\r")
#Calling Function
patten3()