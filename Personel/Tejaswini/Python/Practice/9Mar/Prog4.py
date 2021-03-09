#Join strings by multiple delimiters
test_str1 = input("Enter the string first : ")
test_str2 = input("Enter the second string : ")
  
# printing original strings 
print("The original string 1 is : " + str(test_str1)) 
print("The original string 2 is : " + str(test_str2)) 
  
# initializing join list 
join_list = ["+", "*", "-", "$", ",", "@"] 
  
# + operator used for concatenations 
res = [test_str1 + delim + test_str2 for delim in join_list] 
  
print("\nAll delimiters concatenations :\n " + str(res)) 