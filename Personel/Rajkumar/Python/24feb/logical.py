print("***Logical Operators***")
print("1.And Operater")
print("2.or Operater |")
print("3.Not Operater")
selection=int(input("selection.."))

if(selection==1):
    print("your selection And Operater")
    print("Both condition are true than return a true  value")
    a=int(input("Enter a  Number: "))
    print(a>0 and a<100)
elif(selection==2):
    print("your selection  or operater")
    print("Any one condition  are true than return a true value")
    a=int(input("Enter a First Number: "))
    print(a>0 or a<10)
elif(selection==3):
    print("your selection not operster")
    print("False because not is used to reverse the result")
    a=int(input("Enter a  Number: "))
    print(not(a > 3 and a < 10))