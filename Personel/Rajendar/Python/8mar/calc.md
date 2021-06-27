print("1.Addition \n2.Subtraction \n3.Multipication \n4.Division \n5.Modulus \n6.Exponent")
print("Enter the input in this format- a,b,operator \n")

def calci(a,b,ar):
    if ar == 1 :
        return a+b
    elif ar == 2 :
        return a-b
    elif ar == 3 :        
        return a*b
    elif ar == 4:
        return a/b
    elif ar == 5 :
        return a%b
    elif ar == 6 :
        return a**b
    else:
        print("Enter between 1 to 6")                                              


x,y,z=[float(s) for s in input('Enter : ').split(',')]

print(calci(x,y,z))
