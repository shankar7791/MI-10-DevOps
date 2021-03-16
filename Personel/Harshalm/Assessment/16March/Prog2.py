#Program to print duplicates from a list of integers 

list = input("Enter the list of element :-")

dulpicates = []
interger = {}
for x in list :
    if x not in interger :
        interger[x] = 1
    else :
        if interger[x] == 1 :
            dulpicates.append(x)
        interger[x] += 1
print(dulpicates)
