def star():
    a = 5
    b = 5
    for row in range(0,a+1):
        for col in range(b-row,0,-1):
            print(col,end=" ")
        print()    
star()         