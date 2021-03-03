def palindrome():
    number = int(input("enter the number : "))
    temp = number
    rev = 0
    while(number > 0):
        sum = number % 10
        rev = rev*10+sum
        number = number//10
    if(temp == rev):
        print("number is palindrome")
    else:
        print("number is not palindrome")

palindrome()