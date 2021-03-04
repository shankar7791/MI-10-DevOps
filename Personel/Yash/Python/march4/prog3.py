# Program 3 : Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.

def check(s) :
    countUpper=0
    countLower=0
    for i in strInput :
        if i.isupper() :
            countUpper+=1
        elif i.islower() :
            countLower+=1
        else :
            pass
    print(f"Number of Uppercase letters = {countUpper}")
    print(f"Number of Lowercase letters = {countLower}")

strInput=input("Enter the string : ")
check(strInput)

