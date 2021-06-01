my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print("All keys")

for x in my_dict:
    print(x)
print("All values")

for x in my_dict.values():
    print(x)
print("All keys and values")

for x,y in my_dict.items():
    print(x, ":" , y)