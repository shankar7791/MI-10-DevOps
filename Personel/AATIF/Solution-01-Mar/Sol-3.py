str = input("Enter the String: ")

l = len(str)
p = l-1
Index = 0


while Index < p :
    if str [Index] == str [p]:
        Index += 1
        p -= 1
        print("String is a palindrome.")
        break
    else :
        print("String is not a palindrome.")
        break