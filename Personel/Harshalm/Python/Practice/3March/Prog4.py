#Find length of a string in python using for loop

def findlen(string) :
    counter = 0 
    for i in string :
        counter += 1
    return counter

string = str(input("Enter a string :-"))
print(findlen(string))

