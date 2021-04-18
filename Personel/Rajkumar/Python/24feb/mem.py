print("***Membership Operators***")
print("1.in Operater")
print("2.not in Operater |")
selection=int(input("selection.."))

if(selection==1):
    print("your selection in Operater")
    print("Returns True if a sequence with the specified value is present in the object")
    x = ["apple", "banana"]
    print("banana" in x)
elif(selection==2):
    print("your selection  not in operater")
    a=int(input("EReturns True if a sequence with the specified value is not present in the object "))
    x = ["apple", "banana"]
    print("pineapple" not in x)
