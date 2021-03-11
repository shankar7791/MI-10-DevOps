# Python program create function to check if a string is palindrome or not

 
def palindrome ():
    
    string=str(input("Enter a string:"))
    
    if(string==string[::-1]):
      print("The string is a palindrome")
    else:
      print("Not a palindrome")

palindrome()


