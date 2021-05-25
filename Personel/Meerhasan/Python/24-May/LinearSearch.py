def linear_search(list,n):
    i = 0
    for i in range(len(list)):
        if list[i] == int(n):
            globals()['pos'] = i
            return True
    return False

pos = -1

list = [21,33,45,9,24,9,34,7,88,96,54,35,66,77]

n =input("Find The Number => ")

if linear_search(list,int(n)):
    print(f"\nNumber {n} Is Present At Index =>  {pos+1}")
else:
    print(f"\nNumber {n} Not Found")