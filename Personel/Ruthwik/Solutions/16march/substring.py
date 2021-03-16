# Check if a Substring is Present in a Given String 

def substr_chk(string):
    substr=input("Enter the substring : ")

    if substr in string:
        print(f"{substr} is present in string")
    else:
        print(f"{substr} is not present in string")

s=input('Enter the string : ')
print('eEntered string is : ', s)

substr_chk(s)