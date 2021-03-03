#To create a function to check if the string is palindrome or not 
def palindrome():
    a=input("Enter the string : ")
    b=list(reversed(a))
    if(list(a)==b):
        print("palindrome")
    else:
        print("Not a palindrome")
palindrome()