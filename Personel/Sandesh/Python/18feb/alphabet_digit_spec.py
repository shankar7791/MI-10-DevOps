char = input("Enter Any Character : ")

if (char >="a" and char <="z" ) or (char >="A" and char <="Z" ):
    print(f"{char} is a Alphabet")
elif ( char >= "0" and char <= "9"):
    print(f"{char} is a Digit" )
else : 
    print(f"{char} is Special Character")