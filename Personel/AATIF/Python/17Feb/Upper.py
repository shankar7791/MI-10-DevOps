string = input("Please Enter your Own String : ")
string1 = ''
i = 0

while(i < len(string)): 
    if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]
    i = i + 1
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)