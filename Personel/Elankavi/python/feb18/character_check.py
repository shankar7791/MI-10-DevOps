
#check it is character or alphabet or digits

ch = input("Enter the character : ")
if(ch >= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z'):
    print(ch, "is a character")
elif(ch >= '0' and ch <= '9'):
    print(ch, "is a digit")
else:
    print(ch, "is a special character")