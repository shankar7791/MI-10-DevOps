#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#declarya Function
def case(s):
    #Declary a variable to calculate 
    lower ,upper = 0, 0
    #Logic calculate
    for e in s:
        if(e.islower()):
            lower = lower+1
        elif(e.isupper()):
            upper = upper+1
    #print a Value
    print("Lower case: ",lower)
    print("Upper case: ",upper)
s=str(input("Enter a String Value: "))
#Calling Function
case(s)

