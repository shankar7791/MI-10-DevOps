i= 1
while i <=50 :
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}=fizzbuzz")
        
    elif i % 3 == 0:
        print(f"{i}=fizz")
        
    elif i % 5 == 0:
        print(f"{i}=buzz")
    i = i + 1

        