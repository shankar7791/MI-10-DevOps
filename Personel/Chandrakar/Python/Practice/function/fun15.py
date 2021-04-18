#armstorng number
def armsto_rng():
    a = int(input("enter the number : "))
    sum = 0
    temp = a    
    while temp > 0:
        reminder = temp % 10
        sum = sum + reminder*reminder*reminder
        temp = temp//10
    if a ==sum:
        print(f"{a}  armstrong number ")
    else :
        print(f"{a} not  armstrong number ")       
armsto_rng()    
armsto_rng()