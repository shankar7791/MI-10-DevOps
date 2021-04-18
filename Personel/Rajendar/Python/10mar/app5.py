# Program 1 : write a menu driven Program to
# Perform following operations
# 1. Length of String
# 2. Reverse String
# 3. Check Palindrome or not
# 4. Check Symmetrical or not
# 5. Check Permutations and combination
# 6. Check two strings are anagram or not
# 6. Exit

def len_str(string):
    return len(string)


def rev_str(string):
    return string[::-1]


def Palindrome(string):
    str = string[::-1]
    if string == str:
        return "string is palindrome"
    else:
        return "string is not palindrome"


def Symmetrical(string):
    n = len(string)
    flag = 0

    if n % 2:
        mid = n//2 + 1
    else:
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n):

        if (string[start1] == string[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")


def anagram(string, string1):

    if(sorted(string) == sorted(string1)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


def per_and_com(string):
    import itertools

    p = itertools.permutations(str1)

    for val in p:
        print("Entered string possible permutation: ", *val)

    str2 = input("Enter the string for combinations: ")

    c = itertools.combinations(str2, 2)

    for val in c:
        print("Entered string Possible Combinations: ", *val)


print("***MENU****")
print("1.Length of string")
print("2.reverse string")
print("3.palindrome")
print("4.symmetrical")
print("5.anagram")
print("6.Permutation and combination")
print("7.Exit")

while True:
    choice = input("enter the choice number(1/2/3/4/5/exit) : ")

    if choice in ('1', '2', '3', '4', '5', '6', 'exit'):

        if choice == '1':
            string = str(input("Enter the string : "))
            print("Length of string is = ", len_str(string))

        if choice == '2':
            string = str(input("Enter the string : "))
            print("reverse of string is = ", rev_str(string))

        if choice == '3':
            string = str(input("Enter the string : "))
            print(Palindrome(string))

        if choice == '4':
            string = str(input("Enter the string : "))
            print(Symmetrical(string))

        if choice == '5':
            string = str(input("Enter the string : "))
            string1 = str(input("enter the string: "))
            print(anagram(string, string1))

        if choice == '6':
            str1 = input("Enter the string for permutation: ")
            print(per_and_com(str1))

        if choice == 'exit':
            break
    else:
        print("inavlid choice")
