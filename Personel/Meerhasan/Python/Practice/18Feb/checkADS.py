
#Write a program to check  entered input is  alphabet digit or special character

check = input("Please Enter Your Character : ")

if (check >= 'a' and check <= 'z') or ( check >= 'A' and check <= 'Z') :
    print(f"{check} Is a Alphabet")

elif (check >= '0' and check <= '9') :
    print(f"{check} Is a Digit")

else :
    print(f"{check} Is a Special Character")