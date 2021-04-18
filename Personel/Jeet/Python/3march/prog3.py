#Python program to check whether the string is Symmetrical or Palindrome

def Palin(str):
    if str == str[::-1]:
        print('String is Palindrome')
    else:
        print('string is not palindrome')
    
def Symmetric(str):
    if len(str)%2 == 0:
        mid = int(len(str)/2)
        str1 = str[:mid]
        str2 = str[mid:]
    else:
        mid = int(len(str)//2)
        str1 = str[:mid]
        str2 = str[mid:]
    if str1 == str2:
        print('string is symmetrical')
    else:
        print('string is not symmetrical')


str = input('Enter the string:')
Palin(str)
Symmetric(str)