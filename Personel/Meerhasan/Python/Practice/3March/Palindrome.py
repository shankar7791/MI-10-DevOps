
# Python program create function to check if a string is palindrome or not 

def palindrome() :
    char = str(input("Enter Word : "))

    w = ""
    for i in char :
        w = i + w

    if char == w :
        print(f"{char} Is a Palindrome ")
    else:
        print(f"{w} Is not a Palindrome ")

palindrome()
