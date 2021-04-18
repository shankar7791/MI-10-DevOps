def check(string) : 
    vowels = set("aeiou")
    s = set({})
    for val in string : 
        if val in vowels :
            s.add(val)

    if s == vowels :
        print(f"The entered {string} character is vowel")
    else :
        print(f"The entered {string} character is  not vowel")

string = input("Enter a any Vowel character :  ")

check(string)