#Ceate a Function
def pali():

# Ask for enter the number from the use  
    number = int(input("Enter the integer number: "))  
  
# Initiate value to null  
    revs_number = 0  
    temp_number=number
# reverse the integer number using the while loop  
  
    while (number > 0):  
# Logic  
      remainder = number % 10  
      revs_number = (revs_number * 10) + remainder  
      number = number // 10  
  
# Display the result  
    if(temp_number==revs_number):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
#Calling Function
pali()