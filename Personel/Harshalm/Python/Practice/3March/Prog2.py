#Python program create function to check if a string is palindrome or not 


def palindrome():
    char = str(input("Enter a string :-"))

    word = " "
    for i in char :
        word = i + word
    if char == word :
        print(f"{char} is a palindrome ")
    else :
        print(f"{word} is not a palindrome ")
        
palindrome()
