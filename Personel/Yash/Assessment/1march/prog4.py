# Program 4 : check given string is palindrome or not

strInput = input("Enter the string : ")

if strInput == strInput[::-1] :
  print("Entered string is a Palindrome")
else:
  print("Entered string is not a Palindrome")
