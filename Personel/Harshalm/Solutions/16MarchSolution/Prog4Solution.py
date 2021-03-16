# Remove all duplicates from a given string in Python

#Algorithm
#step1 :- create removeDuplicate function
#step2 :- when s is set of string
#step3 :- when s is join(s)
#step4 :- print the string removing duplicate
#step5 :- create string
#step6 :- removeDuplicate function of a string
#step7 :- exit


#Program

def removeDuplicate(string) :
    s = set(string)
    s = "".join(s)
    print("the string removing duplicate :-", s)

string = input("Enter the string :-")
removeDuplicate(string)



