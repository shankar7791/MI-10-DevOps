def pali():
    i = input('Enter a string:')
    if i == i[::-1]:
        print('String is palindrome')
    else:
        print('String is not palindrome')
pali()