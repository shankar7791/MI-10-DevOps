#pailendron number with decorator

def decor1(num):
    def inner():
        c = num()
        while True:     
            k = str(c)
            if k == k[::-1]:  
                break
            else:
                m = int(k[::-1])
                c += m
        return c
    return inner
@decor1
def num():
    a = int(input("enter the number : "))
    return a
print(num())                   
 