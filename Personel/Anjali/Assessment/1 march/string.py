str = input("Enter a String: ")

string = ''
i = len(str) - 1

while i >= 0:
    string = string + str[i]
    i = i - 1
print(string)

if str == string:
    print("String is Palindrome")
else:
    print("String is not Palindrome") 