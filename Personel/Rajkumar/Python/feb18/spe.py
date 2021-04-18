mn = input("Please Enter Character : ")
if((mn >= 'a' and mn <= 'z') or (mn >= 'A' and mn <= 'Z')): 
    print(f("The Given Character {mn} is an Alphabet")) 
elif (mn>=0 and mn<=9):
    print("The Given Character is an Number",mn) 
else:
    print(f("The Given Character {mn} is a Special Character"))