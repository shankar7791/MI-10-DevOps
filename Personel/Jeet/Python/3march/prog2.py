#Python program create function to check if a string is palindrome or not 

def Palin(str):
    if str == str[::-1]:
        print('String is Palindrome')
    else:
        print('string is not palindrome')

str = input('Enter the string:')
Palin(str)