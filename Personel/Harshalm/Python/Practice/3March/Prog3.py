#Python program to check whether the string is Symmetrical or Palindrome

string = input("Enter the string :-")
def palindrome(string) :
    string1 = list(reversed(string))
    if list(string) == string1 :
        print("palindrome")
    else :
        print("not a palindrome")

def symmetrical(string) :
    n = len(string)
    c = 0
    if n % 2 :
        v = n // 2 + 1
    else :
        v = n // 2
    s1 = 0
    s2 = v
    while s1 < v and s2 < n :
        if string[s1] == string[s2] :
            s2 += 1 
            s1 += 1
        else :
            c = 1
            break 
    if c == 1 :
        print("The string is not a symmetrical")
    else :
        print("The string is symmetrical")  

palindrome(string)
symmetrical(string)
