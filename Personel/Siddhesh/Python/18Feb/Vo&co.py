character = str(input("Enter the character : "))

if character >= 'A' and character <= 'Z' or character >= 'a' and character <= 'z':
    print(f"{character} is a Alphabet")

elif character >= '0' and character <= '100' :
    print(f"{character} is Number")
else:
    print(f"{character} is a special character")