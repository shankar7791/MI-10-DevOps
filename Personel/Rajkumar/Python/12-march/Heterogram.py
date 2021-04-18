#Check whether a given string is Heterogram or not
def stringheterogram(s, n):
    hash = [0] * 26
    for i in range(n):
        if s[i] != ' ':
            if hash[ord(s[i]) - ord('a')] == 0:
             hash[ord(s[i]) - ord('a')] = 1
            else:
             return False
    return True

 
s = input("Enter the String ::>")
n = len(s)
print(s,"This string is Heterogram" if stringheterogram(s, n) else "This string is not Heterogram")