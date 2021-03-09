#Given a string, return the sum and average of the digits that appear in the string, ignoring all other character

def findSum(str1): 
  
    # A temporary str1ing 
    temp = "0"
  
    # holds sum of all numbers 
    # present in the str1ing 
    Sum = 0
  
    # read each character in input string 
    for ch in str1: 
  
        # if current character is a digit 
        if (ch.isdigit()): 
            temp += ch 
  
        # if current character is an alphabet 
        else: 
  
            # increment Sum by number found 
            # earlier(if any) 
            Sum += int(temp) 
  
            # reset temporary str1ing to empty 
            temp = "0"
  
    # atoi(temp.c_str1()) takes care 
    # of trailing numbers 
    return Sum + int(temp) 
  
# Driver code 
  
  
# input alphanumeric str1ing 
str1 = input('enter a string : ')
  
# Function call 
print(findSum(str1)) 
  