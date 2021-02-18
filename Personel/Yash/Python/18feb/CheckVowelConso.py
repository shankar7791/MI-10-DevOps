#Prog 5 :  Write a program to input any alphabets and check it is vowel or consonent
char = input("Enter the Character : ")

if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A'
       or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
    print(f"{char} is a Vowel")
else:
    print(f"{char} is a Consonent")