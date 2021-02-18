# check character, integer or special character

char = input("Please Enter Your Own Character : ")

if((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
    print("The Given Character ", char, "is an Alphabet")
elif(char >= '0' and char <= '9'):
    print("The Given Character ", char, "is a Digit")
else:
    print("The Given Character ", char, "is a Special Character")
