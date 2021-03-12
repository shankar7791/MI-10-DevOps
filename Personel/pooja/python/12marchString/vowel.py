def string_check(string):
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for char in string:
        if char not in vowel:
            print(f"{string}:vowel is not present")
            break
        else:
            print(f"{string}:vowel is present")


string = input("enter the string ")
print(string_check(string))
