from collections import Counter
def string():
    l=str(input("Enter the string : "))
    print()
    print("The string list : \n",Counter(l))
    print()
def number():
    l =input("Enter the numbers : ")
    print()
    print("The numbers list : \n",Counter(l))
    print()

string()
number()
