a = input("Enter the character : ")
if(a >= 'a' and a<= 'z') or (a>= 'A' and a<= 'Z'):
    print(a, "is a character")
elif(a >= '0' and a <= '9'):
    print(a, "is a digit")
else:
    print(a, "is a special character")