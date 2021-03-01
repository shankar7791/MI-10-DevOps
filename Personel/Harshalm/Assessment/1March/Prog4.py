#check given string is palindrome or not

string = input("Enter the string :-")

if string == string[::-1] :
    print("The string is palindrome")
else :
    print("The string is not a palindrome")

