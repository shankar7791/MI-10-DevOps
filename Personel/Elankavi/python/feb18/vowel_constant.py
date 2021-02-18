#program to check the character is vowels or constant

ch = (input("Enter the character : "))
if(ch =='a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(ch, "is a vowel")
elif(ch =='A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(ch, "is a vowel")
else:
    print(ch,"is a constant")