#enter input is alphabet digit or special character


character = str(input("Enter any character : "))

if character >= 'A' and character <= 'Z' or character >= 'a' and character <= 'z' :
    print(f"{character} is Alphabet")
elif character >= '0' and  character <= '1000' :
    print(f"{character} is Numbers")
else :
    print(f"{character} is a special character or symbols")

