n = int(input("No of keys : "))
d1 = dict()
for i in range(n):
    key  = input("Enter the key : ")
    value = input("Enter the value : ")
    d1[key] = value
d2 = dict()
for i in range(n):
    key  = input("Enter the key  for dict2: ")
    value = input("Enter the value for dict2 : ")
    d2[key] = value

def merge(d1,d2):
    return(d1.update(d2))
    
merge(d1,d2)
print("After merge  : ",d1)
