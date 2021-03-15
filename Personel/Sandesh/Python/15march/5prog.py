#Remove all duplicates words from a given sentence

String = input("Enter a word or Statement : ")
i = 0 
S1= ""
for x in String : 
    if String.index(x)== i :
        S1 +=x
        i+=1
print(f"after removing the duplicates from {String} : ", S1)