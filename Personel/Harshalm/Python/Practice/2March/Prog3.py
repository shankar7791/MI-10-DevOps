#number is palindrome or not

def palindrome():
    number = int(input("Enter the number :-"))
    temp = number
    rev = 0
    while number > 0 :
        addition = number % 10
        rev = rev*10 + addition
        number = number // 10
    if temp == rev :
        print("Number is palindrome")
    else :
        print("Number is not palindrome")

palindrome()

