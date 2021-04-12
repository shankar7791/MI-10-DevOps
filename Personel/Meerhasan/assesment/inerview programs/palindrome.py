
s = input("Enter Sequance => ")

def palindrome() :

    rev = s[::-1]

    if s == rev :
        print("Sequance is palindrome")

    else:
        print("Sequance is not palindrome")

    return rev

palindrome()
