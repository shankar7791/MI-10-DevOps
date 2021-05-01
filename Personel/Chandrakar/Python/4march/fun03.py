def u_l(st):
    up = 0
    lo = 0
    for le in st:
        if  le.isupper():
            up += 1
        elif le.islower():
            lo += 1
    print("uper case : ",up)
    print("lower case : ",lo) 
print(u_l("chanDraKAR"))              