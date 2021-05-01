def remov(string_data):
    result=''
    for character in string_data:
	    if character not in result :
	        result=result+character  
    return result
string_data=input("Enter string: ")
print("Befor removing : ",string_data)
print("Final result after removing duplicate characters: \n",remov(string_data) )
  