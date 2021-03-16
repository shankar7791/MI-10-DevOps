#program to print the pattern "A"

def fun():
    b=""    
    for row in range(0,7):    
        for column in range(0,7):     
            if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
                b=b+"*"    
            else:      
                b=b+" "    
        b=b+"\n"    
    print(b)
fun()